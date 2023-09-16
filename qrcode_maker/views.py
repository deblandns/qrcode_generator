from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from . import forms
from . import models


# Create your views here.


def navbar_components(request):
    return render(request, "shared/navbar.html")


class homepage(View):
    def get(self, request):
        form = forms.qrcodes()
        return render(request, "homepage.html", {"form": form})

    def post(self, request):
        form = forms.qrcodes(request.POST)
        if form.is_valid():
            form.save()
            image = models.qrcodes.objects.last()
        return render(request, "homepage.html", {"form": form, "image": image})






