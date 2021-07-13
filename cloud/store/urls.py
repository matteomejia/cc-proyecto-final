from django.contrib import admin
from django.urls import path, include

from .views import (
    AddToCartView,
    OrderSummaryView,
    RemoveFromCartView,
    CheckoutView
)

app_name = 'store'

urlpatterns = [
    path('add-to-cart/<slug>/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/<pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/<pk>/', CheckoutView.as_view(), name='checkout')
]
