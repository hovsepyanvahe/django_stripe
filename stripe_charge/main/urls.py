from django.urls import path
from .views import Home, Charge, Success

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('charge/', Charge.as_view(), name='charge'),
    path('success/<str:args>', Success.as_view(), name='success'),
]

