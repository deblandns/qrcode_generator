from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class donatepage(TemplateView):
    template_name = "donatepage.html"


