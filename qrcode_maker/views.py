from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class homepage(TemplateView):
    template_name = "homepage.html"


def navbar_components(request):
    return render(request, "shared/navbar.html")