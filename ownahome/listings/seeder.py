from listings.models import Listing

def seed_listings():
    sample_data = [
        {
            "title": "Modern 3-Bedroom Apartment in Kilimani",
            "location": "Kilimani, Nairobi",
            "price_cash": 15000000,
            "price_mortgage": 18000000,
            "development_status": "completed",
            "description": "A spacious 3-bedroom apartment with modern amenities.",
            "image_url": "https://plus.unsplash.com/premium_photo-1661915661139-5b6a4e4a6fcc"
        },
        {
            "title": "2-Bedroom Apartment Off-Plan in Westlands",
            "location": "Westlands, Nairobi",
            "price_cash": 12000000,
            "price_mortgage": 14000000,
            "development_status": "offplan",
            "description": "Secure this off-plan deal for a 2-bedroom apartment in Westlands.",
            "image_url": "https://images.unsplash.com/photo-1494526585095-c41746248156"
        },
        {
            "title": "Luxurious Villa in Karen",
            "location": "Karen, Nairobi",
            "price_cash": 35000000,
            "price_mortgage": 40000000,
            "development_status": "completed",
            "description": "A luxurious villa with 5 bedrooms and a private garden.",
            "image_url": "https://plus.unsplash.com/premium_photo-1661915661139-5b6a4e4a6fcc"
        },
        {
            "title": "Affordable 1-Bedroom in Ruaka",
            "location": "Ruaka, Nairobi",
            "price_cash": 4500000,
            "price_mortgage": 5000000,
            "development_status": "under_construction",
            "description": "An affordable 1-bedroom apartment under construction in Ruaka.",
            "image_url": "https://images.unsplash.com/photo-1494526585095-c41746248156"
        },
        {
            "title": "Studio Apartment in Ruiru",
            "location": "Ruiru, Nairobi",
            "price_cash": 2500000,
            "price_mortgage": 3000000,
            "development_status": "completed",
            "description": "A cozy studio apartment ideal for young professionals.",
            "image_url": "https://plus.unsplash.com/premium_photo-1661915661139-5b6a4e4a6fcc"
        },
        {
            "title": "Studio Apartment on Thika Road",
            "location": "Juja, Nairobi",
            "price_cash": 8000000,
            "price_mortgage": 17000000,
            "development_status": "completed",
            "description": "A cozy studio apartment ideal for young professionals.",
            "image_url": "https://plus.unsplash.com/premium_photo-1661915661139-5b6a4e4a6fcc"
        },
        {
            "title": "1 bedroom house in Kileleshwa",
            "location": "Kileleshwa, Nairobi",
            "price_cash": 3900000,
            "price_mortgage": 4800000,
            "development_status": "completed",
            "description": "A cozy studio apartment ideal for young professionals.",
            "image_url": "https://plus.unsplash.com/premium_photo-1661915661139-5b6a4e4a6fcc"
        },
         {
            "title": "1 bedroom house in Kileleshwa",
            "location": "Kileleshwa, Nairobi",
            "price_cash": 8900000,
            "price_mortgage": 10800000,
            "development_status": "completed",
            "description": "A cozy studio apartment ideal for young professionals.",
            "image_url": "https://plus.unsplash.com/premium_photo-1661915661139-5b6a4e4a6fcc"
        },
         {
            "title": "1 bedroom house in Kileleshwa",
            "location": "Kileleshwa, Nairobi",
            "price_cash": 9000000,
            "price_mortgage": 14800000,
            "development_status": "completed",
            "description": "A cozy studio apartment ideal for young professionals.",
            "image_url": "https://plus.unsplash.com/premium_photo-1661915661139-5b6a4e4a6fcc"
        }
    ]

    for data in sample_data:
        Listing.objects.get_or_create(**data)
        print(f"Seeded: {data['title']}")
