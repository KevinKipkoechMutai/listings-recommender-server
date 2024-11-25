from django.urls import path, include
from .views import list_listings, recommend_home

urlpatterns = [
    path('listings/', list_listings, name='list_listings'),
    path('recommend/', recommend_home, name='recommend_home'),
]