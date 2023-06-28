from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import CustomUser, Cart, CartItem, Category, Product, Images, Category_banner

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
  list_display = ("email","first_name", "last_name",)
  
admin.site.register(CustomUser,CustomUserAdmin)

class Category_bannerAdmin(admin.ModelAdmin):
   
  def image_tag(self, obj):
    return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.picture.url))
  list_display = ("category_name","image_tag")

admin.site.register(Category_banner,Category_bannerAdmin)


class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name",)
  
admin.site.register(Category,CategoryAdmin)


class ImagesInline(admin.StackedInline):
    model = Images
    
class ProductAdmin(admin.ModelAdmin):
  inlines = [ImagesInline]

  list_display = ("category","name","price","available")
admin.site.register(Product,ProductAdmin)


class CartAdmin(admin.ModelAdmin):
  list_display = ("user","created_at")
  
admin.site.register(Cart,CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
  list_display = ("cart","product","quantity")
  
admin.site.register(CartItem,CartItemAdmin )
