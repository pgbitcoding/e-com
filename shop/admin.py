from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser, Cart, CartItem, Category, Product

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
  list_display = ("email","first_name", "last_name",)
  
admin.site.register(CustomUser,CustomUserAdmin)


class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name",)
  
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
  
  def image_tag(self, obj):
    return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
  
  list_display = ("category","name","price","image_tag","available")
  
admin.site.register(Product,ProductAdmin)


class CartAdmin(admin.ModelAdmin):
  list_display = ("user","created_at")
  
admin.site.register(Cart,CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
  list_display = ("cart","product","quantity")
  
admin.site.register(CartItem,CartItemAdmin )
