"""
URL configuration for e_com project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path("watchlist_add/<int:pk>",views.watchlist_add,name="watchlist_add"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("watchlist_remove/<str:product>",views.watchlist_remove,name="watchlist_remove"),
    path("logout",views.custom_logout,name="logout"),
    path("about",views.about,name="about"),
    path("womens",views.womens,name="womens"),
    path("mens",views.mens,name="mens"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)