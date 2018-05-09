import pickle
import numpy as np
from ..models import NEIGHBORHOOD_CHOICES, PARTITIONING_CHOICES
import pdb


def load_model():

    sgd = pickle.load(
        open('RealEstateMarketPlace/static/model/sgd.p', 'rb'))
    return sgd


def load_scaler():
    scaler = pickle.load(
        open('RealEstateMarketPlace/static/model/scaler.p', 'rb'))
    return scaler


def predict(raw_info):
    model = load_model()
    info = build_input(raw_info)
    return int(model.predict(info)[0])


def build_input(raw_info):
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

    scaler = load_scaler()
    info = scaler.transform(info)

    return info
