from rest_framework import serializers
from .models import Listing


#listing serializer
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'