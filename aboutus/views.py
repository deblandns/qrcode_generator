from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class About_us_page(TemplateView):
    template_name = "aboutus.html"