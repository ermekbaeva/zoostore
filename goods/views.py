from django.shortcuts import render

def catalog(request):
    context = {
        'title': 'Catalog',
        'goods': [
    {
        "description": "Nite Ize® Pack-A-Poo® Dispenser + Refill Bags 3.6 X 1.8 Inch",
        "price": "$19.54"
    },
    {
        "description": "Nite Ize® Pack-A-Poo® Dispenser + Refill Bags 3.6 X 1.8 Inch 4 Count",
        "price": "$22.87"
    },
    {
        "description": "Earth Rated® Leash Dispenser with 15 Unscented Bags 15 Bags",
        "price": "$11.60"
    },
    {
        "description": "Stall DRY® Absorbent & Deodorizer 40.12 Lbs",
        "price": "$39.60"
    },
    {
        "description": "Tropiclean® Spa Tear Stain Remover for Dog 8 Oz",
        "price": "$22.54"
    },
    {
        "description": "Earth Rated® Unscented Refill Rolls 8 Refill Rolls 120 Bags/8 Rolls",
        "price": "$17.52"
    },
    {
        "description": "Earth Rated® Unscented Compostable Refill Rolls 60 Bags/4 Rolls",
        "price": "$20.17"
    },
    {
        "description": "Earth Rated® Unscented Bags with Handles 120 Bags",
        "price": "$17.35"
    },
    {
        "description": "Earth Rated® Unscented Bags on a Single Roll 300 Bags",
        "price": "$25.78"
    },
    {
        "description": "Earth Rated® Leash Dispenser with 15 Lavender Scented Bags 15 Bags",
        "price": "$11.74"
    },
    {
        "description": "Earth Rated® Lavender Scented Refill Rolls 8 Refill Rolls 120 Bags/8 Rolls",
        "price": "$17.52"
    },
    {
        "description": "Earth Rated® Lavender Scented Bags with Handles 120 Bags",
        "price": "$17.52"
    },
    {
        "description": "Earth Rated® Lavender Scented Bags on a Single Roll 300 Bags",
        "price": "$25.95"
    },
    {
        "description": "Bone Shaped Pet Waste Bag Dispenser",
        "price": "Regular price\n$4.99\nSale pricefrom $2.49\n\n                Save $2.50"
    }
],
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    context = {
        'title': 'Catalog',
        'goods': [
    {
        "description": "Nite Ize® Pack-A-Poo® Dispenser + Refill Bags 3.6 X 1.8 Inch",
        "price": "$19.54"
    },
    {
        "description": "Nite Ize® Pack-A-Poo® Dispenser + Refill Bags 3.6 X 1.8 Inch 4 Count",
        "price": "$22.87"
    },
    {
        "description": "Earth Rated® Leash Dispenser with 15 Unscented Bags 15 Bags",
        "price": "$11.60"
    },
    {
        "description": "Stall DRY® Absorbent & Deodorizer 40.12 Lbs",
        "price": "$39.60"
    },
    {
        "description": "Tropiclean® Spa Tear Stain Remover for Dog 8 Oz",
        "price": "$22.54"
    },
    {
        "description": "Earth Rated® Unscented Refill Rolls 8 Refill Rolls 120 Bags/8 Rolls",
        "price": "$17.52"
    },
    {
        "description": "Earth Rated® Unscented Compostable Refill Rolls 60 Bags/4 Rolls",
        "price": "$20.17"
    },
    {
        "description": "Earth Rated® Unscented Bags with Handles 120 Bags",
        "price": "$17.35"
    },
    {
        "description": "Earth Rated® Unscented Bags on a Single Roll 300 Bags",
        "price": "$25.78"
    },
    {
        "description": "Earth Rated® Leash Dispenser with 15 Lavender Scented Bags 15 Bags",
        "price": "$11.74"
    },
    {
        "description": "Earth Rated® Lavender Scented Refill Rolls 8 Refill Rolls 120 Bags/8 Rolls",
        "price": "$17.52"
    },
    {
        "description": "Earth Rated® Lavender Scented Bags with Handles 120 Bags",
        "price": "$17.52"
    },
    {
        "description": "Earth Rated® Lavender Scented Bags on a Single Roll 300 Bags",
        "price": "$25.95"
    },
    {
        "description": "Bone Shaped Pet Waste Bag Dispenser",
        "price": "Regular price\n$4.99\nSale pricefrom $2.49\n\n                Save $2.50"
    }
],
    }
    return render(request, 'goods/product.html', context)