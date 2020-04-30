from django.shortcuts import render
from django.views import View


class Stripe(View):
    def get(self, request):
        return render(request, 'stripe.html')
