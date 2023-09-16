from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms
# Create your views here.


class Contact_us(View):
    def get(self, request: HttpResponse):
        contact_form = forms.User_contact()
        return render(request, "contactus.html", {"contact_form": contact_form})

    def post(self, request: HttpResponse):
        contact_form = forms.User_contact(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("contact-us")

        return render(request, "contactus.html", {"contact_form": contact_form})


