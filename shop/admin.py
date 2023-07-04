from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import CustomUser, Category, Product, Images, Category_banner, Wishlist, Subcategory, Cart
from .forms import ProductForm

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
    
# class ProductAdmin(admin.ModelAdmin):

#   list_display = ("name","price","available")
# admin.site.register(Product,ProductAdmin)


class ProductAdmin(admin.ModelAdmin):
  inlines = [ImagesInline]
  form = ProductForm

admin.site.register(Product, ProductAdmin)


class WishlistAdmin(admin.ModelAdmin):
  list_display = ("user","product")
  
admin.site.register(Wishlist,WishlistAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
  list_display = ("name",)
    
admin.site.register(Subcategory,SubcategoryAdmin)
    
class CartAdmin(admin.ModelAdmin):
  list_display = ("user","product","quantity")
  
admin.site.register(Cart,CartAdmin)
  