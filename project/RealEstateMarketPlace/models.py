from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import UserManager
from django.core.validators import RegexValidator
# from django.contrib.auth.models import User

NEIGHBORHOOD_CHOICES = (
    ('Aviatiei', 'Aviatiei'),
    ('Berceni', 'Berceni'),
    ('Centru', 'Centru'),
    ('Colentina', 'Colentina'),
    ('Drumul Taberei', 'Drumul Taberei'),
    ('Ferentari', 'Ferentari'),
    ('Giulesti', 'Giulesti'),
    ('Grivita', 'Grivita'),
    ('Magurele', 'Magurele'),
    ('Militari', 'Militari'),
    ('Pantelimon', 'Pantelimon'),
    ('Rahova', 'Rahova'),
    ('Tei', 'Tei'),
    ('Titan', 'Titan'),
    ('Vitan', 'Vitan'),
)

PARTITIONING_CHOICES = (
    ('Circular', 'Circular'),
    ('Decomandat', 'Decomandat'),
    ('Nedecomandat', 'Nedecomandat'),
    ('Semidecomandat', 'Semidecomandat'),
)


class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^\+?\d{10,11}$',
                                 message="Phone number must have exactly 10 digits and optionally begin with '+<international_prefix>' ")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Estate(models.Model):
    address = models.CharField(max_length=100, null=True)
    price = models.FloatField(default=0)
    rooms = models.PositiveSmallIntegerField(default=0)
    floor = models.PositiveSmallIntegerField(default=0)
    size = models.FloatField(default=0)
    estimated_price = models.FloatField(default=0, null=True)
    year = models.PositiveIntegerField(default=1900)
    image = models.ImageField(upload_to='images', null=True, max_length=None)
    bathrooms = models.PositiveSmallIntegerField(default=0)
    partitioning = models.CharField(
        max_length=30, choices=PARTITIONING_CHOICES, default='Aviatiei')
    neighborhood = models.CharField(
        max_length=30, choices=NEIGHBORHOOD_CHOICES, default='Decomandat')


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    estate_id = models.ForeignKey(Estate, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_closed = models.BooleanField(default=False)
    ordering = models.FloatField(default=0, null=True)


class FavoriteListing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'listing_id')

    def __str__(self):
        return self.user_id.email + ' ' + self.listing_id.title


class Message(models.Model):
    message = models.TextField()
    sender_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver')
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.message
