from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from workshop.subscriptions.forms import SubscriptionForm


def subscription(request):

    form = SubscriptionForm()

    return render(request, 'subscriptions/subscription_form.html',{'form': form})

