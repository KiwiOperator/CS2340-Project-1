from django import template

register = template.Library()

@register.filter(name='get_quantity')
def get_cart_quantity(cart, movie_id):
    if not isinstance(cart, dict):  # Ensure cart is a dictionary
        return 0
    return cart.get(str(movie_id), 0)  # Convert movie_id to a string for lookup

@register.filter
def multiply(price, quantity):
    try:
        return float(price) * int(quantity)
    except (ValueError, TypeError):
        return 0