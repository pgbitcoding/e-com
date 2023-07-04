import re
from django.db.models import Q , F
from .models import CustomUser,Product,Category,Category_banner, Wishlist, Cart
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    category_banner = Category_banner.objects.all()
    for banner in category_banner:
        print(banner.picture)
    zipped_data = zip(products, categories)
    context = {'zipped_data': zipped_data}
    extra_data = {"products": products, "categories": categories,"category_banner":category_banner} 
    
    context.update(extra_data)  

    return render(request,"index.html",context)

def womens(request):
    products = Product.objects.filter(category__name="Women’s fashion").select_related("category")
    print("Products ----> ",products)
    return render(request,"womens.html",{"products":products})

def mens(request):
    products = Product.objects.filter(category__name="Men’s fashion").select_related("category")
    print("Products ----> ",products)
    return render(request,"mens.html",{"products":products})

def shop(request):
    products = Product.objects.all().order_by("category")
    
    return render(request,"shop.html",{"products":products})

def contact(request):
    return render(request,"contact.html")

def shop_cart(request):
    carts = Cart.objects.filter(user = request.user)
    return render(request,"shop-cart.html",{"carts":carts})

def product_details(request,pk):
    product = Product.objects.get(id=pk)
    print(product.category) 
    related_products = Product.objects.filter(category = product.category)
    
    return render(request,"product-details.html",{"product":product,"related_products":related_products})

def checkout(request):
    return render(request,"checkout.html")

def about(request):
    return render(request,"about.html")

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
        
        
def custom_logout(request):
    logout(request)
    return redirect("index")
    
    
def wishlist_add(request,pk):
    wishlist = Wishlist()
    
    wishlist.product = Product.objects.get(pk=pk)
    wishlist.user = request.user
    wishlist.save()
    
    return redirect('index')


def wishlist_remove(request,product):
    print(Wishlist.objects.filter(product__name=product))
    Wishlist.objects.get(product__name = product).delete( )
    
    return redirect("wishlist")


@login_required
def wishlist(request):
    wishlists = Wishlist.objects.filter(user=request.user).select_related("product")
    return render(request,"wishlist.html",{"wishlists":wishlists})

def add_cart(request,pk):
    cart = Cart.objects.filter(user=request.user, product=pk).first()
    if cart:
        cart.quantity = F('quantity') + 1
        cart.save()
    else:
        new_cart = Cart(user=request.user, product=pk, quantity=1)
        new_cart.save()
    return redirect('index')

    
