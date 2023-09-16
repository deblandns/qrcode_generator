from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.User_contact)
class User_contact(admin.ModelAdmin):
    pass