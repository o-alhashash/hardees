# Generated by Django 2.1 on 2018-08-16 14:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hardees', '0004_auto_20180816_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='likes',
        ),
        migrations.AddField(
            model_name='item',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]