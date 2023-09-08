from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views import View
from .models import Product

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shop/product_list.html', {'products': products})

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        products = Product.objects.filter(id__in=cart.keys())
        return render(request, 'shop/cart.html', {'products': products, 'cart': cart})

    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + quantity
        request.session['cart'] = cart
        return redirect('cart')

    def remove_from_cart(request, product_id):
        cart = request.session.get('cart', {})
        del cart[str(product_id)]
        request.session['cart'] = cart
        return redirect('cart')

