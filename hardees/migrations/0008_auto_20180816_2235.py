# Generated by Django 2.1 on 2018-08-16 19:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardees', '0007_auto_20180816_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]