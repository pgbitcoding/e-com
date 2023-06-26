import re
from django.db.models import Q
from .models import CustomUser
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password

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

def blog(request):
    return render(request,"blog.html")

# Mobile number validate
def validate_mobile_number(mobile_number):
    pattern = r'^\+?[1-9]\d{1,10}$'
    
    if re.match(pattern, mobile_number):
        return True
    else:
        return False

# registration
def registration(request):
    error_messages = []
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')

        # Username exits validation
        if CustomUser.objects.filter(username=username).exists():
            error_messages.append('This username is already in use.')
            
        # Email match validation
        if CustomUser.objects.filter(email=email).exists():
            error_messages.append('this email address is already register')
        
        # Password match validation
        if password != c_password:
            error_messages.append('Both password should be same.')

        # Password length validation
        if len(password) < 6:
            error_messages.append('Password should be at least 6 characters long.')

        # Mobile number validation
        if not validate_mobile_number(mobile):
            error_messages.append('Invalid mobile number.')

        if error_messages:
            context = {
                'error_messages': error_messages
            }
            return render(request, 'index.html', context)

        # Rest of your registration logic
        user = CustomUser(
            email=email,
            first_name=firstname,
            last_name=lastname,
            username=username,
            address=address,
            mobile=mobile
        )
        user.set_password(password)
        user.save()

        return HttpResponse("Success")

    return render(request, 'index.html')    

# login
def login(request):
    error_messages = []
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        hashed_password = ""

        if CustomUser.objects.filter(username=username):
            if check_password(password, hashed_password):
                print("---->allcorrect")
                return render(request, 'index.html')
            else:
                error_messages.append("Password is wrong")    
        else :
            error_messages.append("Username/email is wrong")    
    
        context = {
            "error_messages" : error_messages,
        }    
        return render(request, 'index.html', context)
    return render(request, 'index.html')
        
