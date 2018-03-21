from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Estate)
admin.site.register(FavoriteListing)
admin.site.register(Message, MessageAdmin)
