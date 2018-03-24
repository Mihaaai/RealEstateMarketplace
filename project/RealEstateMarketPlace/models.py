from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import UserManager
# from django.contrib.auth.models import User

CITY_CHOISES = (
    ('Bucuresti', 'Bucuresti'),
    ('Timisoara', 'Timisoara'),
    ('Iasi', 'Iasi'),
    ('Ploiesti', 'Ploiesti'),
    ('Pitesti', 'Pitesti'),
    ('Cluj', 'Cluj'),
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Estate(models.Model):
    city = models.CharField(max_length=20, choices=CITY_CHOISES)
    address = models.CharField(max_length=50, null=True)
    price = models.FloatField(default=0)
    rooms = models.PositiveSmallIntegerField(default=0)
    floor = models.PositiveSmallIntegerField(default=0)
    size = models.FloatField(default=0)
    estimated_price = models.FloatField(null=True)
    year = models.PositiveIntegerField(default=1900)
    distance_to_centre = models.FloatField(null=True)
    image = models.ImageField(upload_to='images', null=True, max_length=None)

    def __str__(self):
        return self.address


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class FavoriteListing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'listing_id')

    def __str__(self):
        return self.user_id.email + ' ' + self.listing_id.title


class Message(models.Model):
    message = models.TextField()
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.message
