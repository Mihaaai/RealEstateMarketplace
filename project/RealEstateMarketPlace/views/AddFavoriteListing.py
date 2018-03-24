from django.shortcuts import redirect
from ..models import FavoriteListing, Listing


def add_favorite_listing(request, listing_id):
    if request.user.is_authenticated:
        if listing_id is not None:
            try:
                fav_listing = FavoriteListing.objects.get(user_id=request.user.id, listing_id=listing_id)
            except FavoriteListing.DoesNotExist:
                fav_listing = None

            if fav_listing is None:
                fav_listing = FavoriteListing(user_id=request.user,
                                              listing_id=Listing.objects.get(id=listing_id))
                fav_listing.save()
            else:
                fav_listing.delete()
        else:
            return redirect('404.html')
    else:
        return redirect('404.html')

    return redirect('details_listing', pk=listing_id)
