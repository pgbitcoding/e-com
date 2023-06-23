from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def shop(request):
    return render(request,"shop.html")

def contact(request):
    return render(request,"contact.html")

def shop_cart(request):
    return render(request,"shop-cart.html")

def product_details(request):
    return render(request,"product-details.html")

def checkout(request):
    return render(request,"checkout.html")

def blog_details(request):
    return render(request,"blog-details.html")