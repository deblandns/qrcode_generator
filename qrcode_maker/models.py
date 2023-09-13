from django.db import models


# Create your models here.


class qrcodes(models.Model):
    text_input = models.CharField(max_length=500, verbose_name="ورودی متن", null=True, blank=True)

    def __str__(self):
        return self.text_input

    class Meta:
        verbose_name = "کد کیو آر"
        verbose_name_plural = "کد های کی آر"


class userqrimages(models.Model):
    image = models.ImageField(upload_to="qrcode/")

    class Meta:
        verbose_name = "تصاویر کیو ار کد کاربر"
        verbose_name_plural = "تصویر های کیو آر کد کاربران"
