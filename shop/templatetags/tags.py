from django import template

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
