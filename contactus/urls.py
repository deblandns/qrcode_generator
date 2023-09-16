from django.urls import path
from . import views

urlpatterns = [
    path("", views.Contact_us.as_view(), name="contact-us")
]