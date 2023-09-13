from django.urls import path
from . import views

urlpatterns = [
    path("", views.donatepage.as_view(), name="donatepage")
]