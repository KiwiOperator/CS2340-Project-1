from django.shortcuts import render, get_object_or_404, redirect
from movies.models import Movie
from .utils import calculate_cart_total
from .models import Order, Item
from django.contrib.auth.decorators import login_required

def index(request):
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict):  # Ensure cart is a dictionary
        request.session['cart'] = {}  # Reset cart to empty dictionary
        cart = {}

    movie_ids = list(cart.keys())
    movies_in_cart = Movie.objects.filter(id__in=movie_ids) if movie_ids else []
    cart_total = calculate_cart_total(cart, movies_in_cart)

    template_data = {
        'title': 'Cart',
        'movies_in_cart': movies_in_cart,
        'cart_total': cart_total,
    }
    return render(request, 'cart/index.html', {'template_data': template_data})


def add(request, id):
    movie = get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict):  # Ensure cart is a dictionary
        cart = {}

    quantity = request.POST.get('quantity', 1)  # Default to 1 if not provided
    try:
        quantity = int(quantity)
        if quantity < 1:
            raise ValueError
    except ValueError:
        quantity = 1  # Fallback to 1 if invalid input

    cart[str(id)] = quantity
    request.session['cart'] = cart  # Ensure cart is properly stored
    return redirect('cart:index')


def remove_movie(request, movie_id):
    cart = request.session.get('cart', {})
    if str(movie_id) in cart:
        del cart[str(movie_id)]
        request.session['cart'] = cart
    return redirect('cart:index')

def clear(request):
    request.session['cart'] = {}
    return redirect('cart:index')

@login_required
def purchase(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart:index')

    movies_in_cart = Movie.objects.filter(id__in=cart.keys())
    cart_total = calculate_cart_total(cart, movies_in_cart)
    order = Order.objects.create(user=request.user, total=cart_total)
    order.save()
    for movie in movies_in_cart:
        Item.objects.create(
            movie=movie,
            price=movie.price,  # Ensure price is set correctly
            order=order,
            quantity=cart[str(movie.id)]
        )
    order.movie.set(movies_in_cart)
    request.session['cart'] = {}

    return render(request, 'cart/purchase.html', {
        'template_data': {'title': 'Purchase Confirmation', 'order_id': order.id}
    })