from django.db import models


class User(models.Model):
    first_name  = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Estate(models.Model):
    address = models.CharField(max_length=500)
    price = models.FloatField()
    rooms = models.IntegerField()
    floor = models.IntegerField(default=0)
    size = models.FloatField()
    estimated_price = models.FloatField(blank=True)
    year = models.IntegerField()
    distance_to_centre = models.FloatField()
    
    
class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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