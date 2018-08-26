# Generated by Django 2.1 on 2018-08-16 13:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hardees', '0002_auto_20180814_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
