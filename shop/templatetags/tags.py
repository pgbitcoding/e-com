from django import template
from decimal import Decimal
        
register = template.Library()

@register.filter
def get_category_class(category_name):
    category_classes = {
        'Women’s fashion': 'women',
        'Men’s fashion': 'men',
        'Kid’s fashion': 'kid',
        'Accessories': 'accessories',
        'Cosmetics': 'cosmetic',
    }
    return category_classes.get(category_name, '')



@register.filter
def apply_discount(price):
    discount = price * Decimal(0.1)  
    discounted_price = price - discount  
    return round(discounted_price, 2)  
