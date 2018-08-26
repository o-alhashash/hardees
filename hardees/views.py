import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ItemForm
from .models import Item


class ItemListView(ListView):
    template_name = 'items.html'
    model = Item


class ItemDetailView(DetailView):
    template_name = 'item_detail.html'
    model = Item


class CreateItemFormView(CreateView):
    template_name = 'createItem.html'
    form_class = ItemForm
    success_url = '/items/'


class UpdateItemFormView(UpdateView):
    model = Item
    fields = '__all__'
    template_name = 'updateItem.html'


class DeleteItemView(DeleteView):
    model = Item
    success_url = '/items/'
    template_name = 'DeleteItem.html'


def likeItem(request):
    if request.method == 'POST':
        item_id = request.POST.get('id', None)
        user = request.user
        try:
            item = Item.objects.get(id=item_id)
        except ObjectDoesNotExist:
            return HttpResponse(404)

        if item.likes.filter(id=user.id).exists():
            item.likes.remove(user)
        else:
            item.likes.add(user)

    context = {
        'likes': item.total_likes,
    }

    return HttpResponse(json.dumps(context), content_type='application/json')
