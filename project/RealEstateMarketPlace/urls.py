from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('add/', views.AddListingView.as_view(), name='add'),
    path('list/', views.ListListingsView.as_view(), name='list_listings'),
    path('list/my-listings/open', views.ListMyListingsView.as_view(), name='list_my_listings'),
    path('list/my-listings/closed', views.ListMyClosedListingsView.as_view(), name='list_my_closed_listings'),
    path('list/<int:pk>', views.DetailListingView.as_view(), name='details_listing'),
    path('list/<int:pk>/delete', views.DeleteListingView.as_view(), name='delete_listing'),
    path('list/<listing_id>/favorite', views.AddFavoriteListingAPI.as_view(), name='favorite'),
    path('list/favorites', views.ListMyFavoriteListingsView.as_view(), name='fav_listings'),
    path('list/search/', views.SearchListListingsView.as_view(), name='search_listings'),
    path('list/<int:pk>/update', views.UpdateListingView.as_view(), name='update_listing'),
    path('list/<listing_id>/message', views.AddMessageAPI.as_view(), name='message'),
]
