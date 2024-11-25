from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Listing
from .serializers import ListingSerializer
from decimal import Decimal

#get listings
@api_view(['GET'])
def list_listings(request):
    location = request.GET.get('location')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    development_status = request.GET.get('development_status')

    listings = Listing.objects.all()

    if location:
        listings = listings.filter(location__icontains=location)
    if min_price:
        listings = listings.filter(price_cash__gte=min_price)
    if max_price:
        listings = listings.filter(price_cash__lte=max_price)
    if development_status:
        listings = listings.filter(development_status=development_status)


#recommend a suitable home to buy based on affordability
@api_view(['POST'])
def recommend_home(request):
    data = request.data
    salary = Decimal(data['salary'])
    existing_loans = Decimal(data['existing_loans'])
    savings = Decimal(data.get('savings', 0))
    listing_id = data['listing_id']

    listing = get_object_or_404(Listing, id=listing_id)

    #subtract loans from salary to determine whether the user can afford the mortgage
    disposal_income = salary - existing_loans
    affordable_mortgage_payment = disposal_income * Decimal(0.30)

    #give appropriate recommendation based on affordability
    recommendation = {}

    if savings >= listing.price_cash:
        recommendation = {
            'option': 'cash',
            'reason': 'You have sufficient savings to buy this property.'
        }
    elif affordable_mortgage_payment >= listing.price_mortgage:
        recommendation = {
            'option': 'mortgage',
            'reason': 'You can afford the monthly mortgage payments.'
        }
    else:
        recommendation = {
            'option': 'neither',
            'reason': 'The property is not presently affordable given your financial situation.'
        }
    
    return Response(recommendation)
    

