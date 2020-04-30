from django.urls import path
from .views import Stripe

urlpatterns = [
    path('', Stripe.as_view(), name='stripe'),
]

