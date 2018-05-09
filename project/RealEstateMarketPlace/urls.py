from django.urls import path

from . import views


urlpatterns = [
    # authentication
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # create 
    path('add/', views.AddListingView.as_view(), name='add'),
    path('<listing_id>/message/', views.AddMessageAPI.as_view(), name='message'),
    # read
    path('', views.ListListingsView.as_view(), name='list_listings'),
    path('my-listings/open/', views.ListMyListingsView.as_view(), name='list_my_listings'),
    path('my-listings/closed/', views.ListMyClosedListingsView.as_view(), name='list_my_closed_listings'),
    path('<int:pk>/', views.DetailListingView.as_view(), name='details_listing'),
    path('search/', views.SearchListListingsView.as_view(), name='search_listings'),
    path('favorites/', views.ListMyFavoriteListingsView.as_view(), name='fav_listings'),
    path('inbox/', views.ListConversationsView.as_view(), name='inbox' ),
    path('conversation/<int:pk>/<int:user_id>/', views.DetailConversationView.as_view(), name='details_conversation'),
    # update
    path('<listing_id>/favorite/', views.AddFavoriteListingAPI.as_view(), name='favorite'),
    path('<int:pk>/update/', views.UpdateListingView.as_view(), name='update_listing'),
    path('profile/<int:pk>/update/',views.UpdateProfileView.as_view(),name='update_profile'),
    path('<listing_id>/close/',views.CloseListingAPI.as_view(),name='close_listing'),
    # delete
    path('<int:pk>/delete/', views.DeleteListingView.as_view(), name='delete_listing'),

]
