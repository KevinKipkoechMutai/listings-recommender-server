from django.urls import path
from .views import list_listings, recommend_listings, create_property, delete_listing

urlpatterns = [
    path('listings/', list_listings, name='list_listings'),
    path('create-listing/', create_property, name='create_listing'),
    path('recommend/', recommend_listings, name='recommend_listings'),
    path('delete-listing/<int:listing_id>', delete_listing, name='delete_listings')
]