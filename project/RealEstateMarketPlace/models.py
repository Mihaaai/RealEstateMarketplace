from django.db import models
from django.contrib.auth.models import User


class Estate(models.Model):
    CITY_CHOISES = (
        ('Bucuresti', 'Bucuresti'),
        ('Timisoara', 'Timisoara'),
        ('Iasi', 'Iasi'),
        ('Ploiesti', 'Ploiesti'),
        ('Pitesti', 'Pitesti'),
        ('Cluj', 'Cluj'),
    )

    city = models.CharField(max_length=20, choices=CITY_CHOISES)
    price = models.FloatField(default=0)
    rooms = models.PositiveSmallIntegerField(default=0)
    floor = models.PositiveSmallIntegerField(default=0)
    size = models.FloatField(default=0)
    estimated_price = models.FloatField(null=True)
    year = models.PositiveIntegerField(default=1900)
    distance_to_centre = models.FloatField(null=True)
    image = models.ImageField(upload_to='images', null=True, max_length=None)


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=20, unique=True)
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class FavoriteListing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Message(models.Model):
    message = models.TextField()
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.message
