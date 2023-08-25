from django.urls import path
from payment.views import *

urlpatterns = [
    path("", home, name="home"),
    path("paypal-reverse", paypal_reverse, name="paypal-reverse"),
    path("paypal-cancel", paypal_cancel, name="paypal-cancel"),
    
]

