from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True, )
    description = models.TextField(max_length=255, )
    pic = models.ImageField(blank=True, null=True, )
    price = models.DecimalField(decimal_places=2, max_digits=6, )

    def get_absolute_url(self):
        return reverse('item-detail', args=[int(self.id)])
