from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    # authentication
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # create 
    path('add/', views.AddListingView.as_view(), name='add'),
    # read
    path('list/', views.ListListingsView.as_view(), name='list_listings'),
    path('list/my-listings/open', views.ListMyListingsView.as_view(), name='list_my_listings'),
    path('list/my-listings/closed', views.ListMyClosedListingsView.as_view(), name='list_my_closed_listings'),
    path('list/<int:pk>', views.DetailListingView.as_view(), name='details_listing'),
    path('list/search/', views.SearchListListingsView.as_view(), name='search_listings'),
    path('list/favorites', views.ListMyFavoriteListingsView.as_view(), name='fav_listings'),
    # update
    path('list/<listing_id>/favorite', views.AddFavoriteListingAPI.as_view(), name='favorite'),
    path('list/<int:pk>/update', views.UpdateListingView.as_view(), name='update_listing'),
    path('profile/<int:pk>/update',views.UpdateProfileView.as_view(),name='update_profile'),
    path('list/<listing_id>/close',views.CloseListingAPI.as_view(),name='close_listing'),
    # delete
    path('list/<int:pk>/delete', views.DeleteListingView.as_view(), name='delete_listing'),
]
