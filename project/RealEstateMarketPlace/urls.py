from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='default'),

    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('add/', views.AddListingView.as_view(), name='add'),
    path('list/', views.ListListingsView.as_view(), name='list_listings'),
]
