from django.urls import path
from . import views

urlpatterns = [
    path("", views.About_us_page.as_view(), name="about-us")
]