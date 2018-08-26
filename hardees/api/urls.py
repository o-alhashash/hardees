from django.urls import path

from .views import (
    ItemCreateAPIView,
    ItemDeleteAPIView,
    ItemDetailAPIView,
    ItemListAPIView,
    ItemUpdateAPIView
)

urlpatterns = [
    path('list/', ItemListAPIView.as_view(), name='items-list'),
    path('detail/<pk>', ItemDetailAPIView.as_view(), name='item-detail'),
    path('create/', ItemCreateAPIView.as_view(), name='item-create'),
    path('update/<pk>/', ItemUpdateAPIView.as_view(), name='item-update'),  # This can be embedded in retrieve update
    path('delete/<pk>/', ItemDeleteAPIView.as_view(), name='item-update'),
]
