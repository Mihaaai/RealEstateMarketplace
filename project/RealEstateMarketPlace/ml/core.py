import pickle
import numpy as np
from ..models import NEIGHBORHOOD_CHOICES, PARTITIONING_CHOICES, Estate, Listing
import pdb


def load_model():

    sgd = pickle.load(
        open('RealEstateMarketPlace/static/model/sgd.p', 'rb'))
    return sgd


def load_scaler():
    scaler = pickle.load(
        open('RealEstateMarketPlace/static/model/scaler.p', 'rb'))
    return scaler


def predict(raw_info, model=None):
    if not model:
        model = load_model()
    scaler = load_scaler()
    info = build_input(raw_info, scaler)
    return int(model.predict(info)[0])


def build_input(raw_info, scaler):
    info = np.array([
        raw_info['year'], raw_info['floor'], raw_info['bathrooms'],
        raw_info['rooms'], raw_info['size']
    ])

    partitioning_array = np.zeros(4)
    neighborhood_array = np.zeros(15)

    index_partitioning = PARTITIONING_CHOICES.index(
        (raw_info['partitioning'], raw_info['partitioning']))
    index_neighborhood = NEIGHBORHOOD_CHOICES.index(
        (raw_info['neighborhood'], raw_info['neighborhood']))

    partitioning_array[index_partitioning] = 1
    neighborhood_array[index_neighborhood] = 1

    info = np.append(info, partitioning_array)
    info = np.append(info, neighborhood_array)
    info = info.reshape(1, -1)

    info = scaler.transform(info)

    return info


def retrain():
    untrained_estates = Estate.objects.filter(trained=False)
    model = load_model()
    scaler = load_scaler()
    train = np.array([])
    prices = np.array([])
    pdb.set_trace()
    for estate in untrained_estates:
        raw_info = {
            'year': estate.year,
            'bathrooms': estate.bathrooms,
            'floor': estate.floor,
            'rooms': estate.rooms,
            'size': estate.size,
            'neighborhood': estate.neighborhood,
            'partitioning': estate.partitioning,
        }

        info = build_input(raw_info, scaler)
        prices = np.append(prices, [estate.price])

        if len(train) == 0:
            train = info
        else:
            train = np.append(train, info, axis=0)

        estate.trained = True
        estate.save()

    model.fit(train, prices)

    del untrained_estates

    listings = Listing.objects.all()

    for listing in listings:
        estate = listing.estate_id
        if estate:
            raw_info = {
                'year': estate.year,
                'bathrooms': estate.bathrooms,
                'floor': estate.floor,
                'rooms': estate.rooms,
                'size': estate.size,
                'neighborhood': estate.neighborhood,
                'partitioning': estate.partitioning,
            }

            new_estimated = predict(raw_info, model)

            estate.estimated_price = new_estimated
            estate.save()
            listing.ordering = new_estimated-estate.price
            listing.save()

    pickle.dump(model, open('RealEstateMarketPlace/static/model/sgd.p', 'wb'))
