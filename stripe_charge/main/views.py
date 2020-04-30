from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

import stripe

stripe.api_key = "sk_test_VYI3Pd5bM9bcdOxXLqvkWzkG00sjXVZS4S"


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class Charge(View):
    def post(self, request):
        amount = 10

        customer = stripe.Customer.create(
            email=request.POST.get('email'),
            name=request.POST.get('name'),
            source=request.POST.get('stripeToken')
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=500,
            currency='usd',
            description='Donation'
        )

        return redirect(reverse('success', args=[amount]))


class Success(View):
    def get(self, request, args):
        amount = args
        context = {
            'amount': amount,
        }
        return render(request, 'success.html', context)
