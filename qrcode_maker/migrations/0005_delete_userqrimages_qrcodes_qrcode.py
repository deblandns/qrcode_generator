# Generated by Django 4.1.3 on 2023-09-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode_maker', '0004_userqrimages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userqrimages',
        ),
        migrations.AddField(
            model_name='qrcodes',
            name='qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='media/qrimages/'),
        ),
    ]
