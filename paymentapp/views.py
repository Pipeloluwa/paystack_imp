from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . import forms
from django.conf import settings
from .models import Payment
from django.contrib import messages
# Create your views here.


def initiate_payment(request: HttpResponse) -> HttpResponse:
    if request.method == "POST":
        payment_form= forms.PaymentForm(request.POST)
        if payment_form.is_valid:
            payment= payment_form.save()
            return render(request, "make_payment.html", {"payment": payment , "paystack_public_key": settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form=forms.PaymentForm()
    return render(request, "initiate_payment.html", {"payment_form":payment_form})

def verify_payment(request: HttpRequest, ref: str) -> HttpResponse: #the hypen and greater than means return
    payment= get_object_or_404(Payment, ref=ref)
    verified= payment.verify_payment()
    if verified:
        messages.success(request, "Verification Successfull")
    else:
        messages.error(request, "Verification Failed.")
    return redirect("initiate-payment")