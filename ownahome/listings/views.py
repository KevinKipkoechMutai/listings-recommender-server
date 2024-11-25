from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer
from .utils import calculate_monthly_mortgage

#get listings
@api_view(['GET'])
def list_listings(request):
    try:
        # filters for query parameters
        location = request.GET.get('location')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        development_status = request.GET.get('development_status')

        #fetch all listings
        listings = Listing.objects.all()

        #apply filters
        if location:
            listings = listings.filter(location__icontains=location)
        if min_price:
            listings = listings.filter(price_cash__gte=float(min_price))  # Cast to float
        if max_price:
            listings = listings.filter(price_cash__lte=float(max_price))  # Cast to float
        if development_status:
            listings = listings.filter(development_status=development_status)

        #serialize the data
        serializer = ListingSerializer(listings, many=True)

        return Response(serializer.data)
    except Exception as e:
        print(f"Error: {e}")
        return Response({"error": "Something went wrong!"}, status=500)


#recommend a suitable home to buy based on affordability
@api_view(['POST'])
def recommend_listings(request):
    try:
        #extract user input
        salary = float(request.data.get('salary', 0))
        existing_loans = float(request.data.get('existing_loans', 0))
        savings = float(request.data.get('savings', 0))

        if salary <= 0:
            return Response({"error": "Salary must be greater than 0"}, status=400)

        #computing the affordable mortgage budget
        disposable_income = salary - existing_loans
        
        # assumed values for mortgage calculation
        annual_interest_rate = 10
        loan_term_years = 20

        # recommended listings based on cash
        affordable_cash_listings = Listing.objects.filter(price_cash__lte=savings)

        # initialize mortgage listings
        affordable_mortgage_listings = [
            listing for listing in affordable_cash_listings 
            if calculate_monthly_mortgage(float(listing.price_mortgage), annual_interest_rate, loan_term_years) <= disposable_income
        ]

        #serializing the data
        cash_serializer = ListingSerializer(affordable_cash_listings, many=True)
        mortgage_serializer = ListingSerializer(affordable_mortgage_listings, many=True)

        return Response({
            "disposable_income": disposable_income,
            "cash_affordable_listings": cash_serializer.data,
            "mortgage_affordable_listings": mortgage_serializer.data
        })
    
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
#create a new listing
@api_view(['POST'])
def create_property(request):
    serializer = ListingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#delete a listing
@api_view(['DELETE'])
def delete_listing(request, listing_id):
    #find and delete listing
    try:
        listing = Listing.objects.get(id=listing_id)
        listing.delete()
        return Response({"messgae": "Listing deleted successfully."}, status=204)
    #handle exception
    except Listing.DoesNotExist:
        return Response({"error": "Listing not found"})
