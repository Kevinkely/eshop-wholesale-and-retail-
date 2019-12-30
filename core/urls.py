from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    add_wholesaler_to_cart,
    remove_from_cart,
    remove_wholesaler_from_cart,
    remove_single_item_from_cart,
    remove_single_wholesaler_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    WholesalerView,
    WholesalerDetailView,
    PaymentViewC
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('wholesalers/', WholesalerView.as_view(), name='wholesalers'),
    path('wholesaler/<slug>/', WholesalerDetailView.as_view(), name='wholesaler'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-wholesaler-to-cart/<slug>/', add_wholesaler_to_cart, name='add-wholesaler-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-wholesaler-from-cart/<slug>/', remove_wholesaler_from_cart, name='remove-wholesaler-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('remove-wholesaler-from-cart/<slug>/', remove_single_wholesaler_from_cart,
         name='remove-single-wholesaler-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('paymentc/<payment_option>/', PaymentViewC.as_view(), name='paymentc'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
