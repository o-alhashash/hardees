from django.views.generic import ListView, DetailView

from .models import Item


class ItemListView(ListView):
    template_name = 'items.html'
    model = Item


class ItemDetailView(DetailView):
    template_name = 'item_detail.html'
    model = Item
