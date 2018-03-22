from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),

    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('add/', views.AddListingView.as_view(), name='add'),
    path('list/', views.ListListingsView.as_view(), name='list_listings'),
    path('profile/<int:pk>/my-listings/', views.ListMyListingsView.as_view(), name='list_my_listings'),
    path('list/<int:pk>',views.DetailListingView.as_view(),name="details_listing"),
    path('list/<int:pk>/delete',views.DeleteListingView.as_view(),name="delete_listing"),
    path('favorite/',views.AddFavoriteListingView.as_view(),name="add_favorite_listing")
]
