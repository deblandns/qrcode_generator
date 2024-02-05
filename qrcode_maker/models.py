from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.


class qrcodes(models.Model):
    qrcode_id = models.AutoField(primary_key=True)
    text_input = models.CharField(max_length=500, verbose_name="ورودی متن", null=True, blank=True)
    qrcode = models.ImageField(upload_to="media/qrimages/", null=True, blank=True)

    def __str__(self):
        return str(self.text_input)

    class Meta:
        verbose_name = "کد کیو آر"
        verbose_name_plural = "کد های کی آر"

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.text_input)
        canvas = Image.new("RGB", (1000, 1000), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        file_name = f'qrcode{self.text_input}"+".png'
        buffer = BytesIO()
        if "http" in file_name:
            changed_file_name = file_name("r" + f'{file_name}')
            self.qrcode.save(changed_file_name, File(buffer), save=False)
        buffer = BytesIO()
        canvas.save(buffer, "png")
        self.qrcode.save(file_name, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
