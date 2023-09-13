from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from . import forms
import qrcode
from . import models


# Create your views here.


def navbar_components(request):
    return render(request, "shared/navbar.html")


class homepage(View):
    def get(self, request):
        QrCodeForm = forms.qrcodes()
        image = "qrcode_maker/static/images/qrcodes/qrcoderesult.png"
        return render(request, "homepage.html", {"qrform": QrCodeForm, "image": image})

    def post(self, request):
        QrCodeForm = forms.qrcodes(request.POST)
        if QrCodeForm.is_valid():
            QrCodeForm.save()
            qrcodetext = models.qrcodes.objects.last()
            img = qrcode.make(qrcodetext)
            type(img)
            img.save("media/qrcode.png")
            return render(request, "homepage.html", {"qrform": QrCodeForm})





