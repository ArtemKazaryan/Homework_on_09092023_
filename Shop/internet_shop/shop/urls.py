from django.urls import path
from .views import ProductListView, CartView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]