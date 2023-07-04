from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("shop",views.shop,name="shop"),
    path("contact",views.contact,name="contact"),
    path("shop_cart",views.shop_cart,name="shop_cart"),
    path("checkout",views.checkout,name="checkout"),
    path("product_details/<int:pk>",views.product_details,name="product_details"),
    path("blog_details",views.blog_details,name="blog_details"),
    path("blog",views.blog,name="blog"),
    path("registration",views.registration,name="registration"),
    path("login",views.login,name="login"),
    path("wishlist_add/<int:pk>",views.wishlist_add,name="wishlist_add"),
    path("wishlist",views.wishlist,name="wishlist"),
    path("wishlist_remove/<str:product>",views.wishlist_remove,name="wishlist_remove"),
    path("logout",views.custom_logout,name="logout"),
    path("about",views.about,name="about"),
    path("womens",views.womens,name="womens"),
    path("mens",views.mens,name="mens"),
    path("add_cart/<int:pk>",views.add_cart,name="add_cart"),
    path("add_cart",views.add_cart,name="add_cart"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)