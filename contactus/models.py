from django.db import models

# Create your models here.


class User_contact(models.Model):
    fullname = models.CharField(max_length=300, verbose_name="نام کامل")
    email = models.EmailField(max_length=400, verbose_name="ایمیل شما")
    message = models.TextField(max_length=2000, verbose_name="متن شما")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "ارتباط با ما"
        verbose_name_plural = "ارتباط ها با ما "
        default_related_name = "ارتباط با ما"