from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from hardees.models import Item

from .serializers import DetailSerializer, ListSerializer


class ItemListAPIView(ListAPIView):
    serializer_class = ListSerializer
    queryset = Item.objects.all()


class ItemDetailAPIView(RetrieveAPIView):
    serializer_class = DetailSerializer
    queryset = Item.objects.all()


class ItemCreateAPIView(CreateAPIView):
    serializer_class = DetailSerializer


class ItemUpdateAPIView(UpdateAPIView):
    serializer_class = DetailSerializer
    queryset = Item.objects.all()


class ItemDeleteAPIView(DestroyAPIView):
    queryset = Item.objects.all()
