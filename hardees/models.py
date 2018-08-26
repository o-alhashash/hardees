from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True, )
    description = models.TextField(max_length=255, )
    pic = models.ImageField(blank=True, null=True, )
    price = models.DecimalField(decimal_places=2, max_digits=6, )
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )

    def get_absolute_url(self):
        return reverse('item-detail', args=[int(self.id)])

    @property
    def total_likes(self):
        return self.likes.count()
