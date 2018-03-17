from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Estate)
admin.site.register(FavoriteListing)
admin.site.register(Message)