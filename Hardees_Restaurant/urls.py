from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from hardees.views import (
    CreateItemFormView,
    DeleteItemView,
    ItemListView,
    ItemDetailView,
    likeItem,
    UpdateItemFormView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', ItemListView.as_view(), name='items'),
    path('items/<slug:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('create/item/', CreateItemFormView.as_view(), name='item-create'),
    path('update/item/<pk>/', UpdateItemFormView.as_view(), name='item-update'),
    path('delete/item/<pk>/', DeleteItemView.as_view(), name='item-delete'),
    path('like_item/', likeItem, name='like-item'),
    path('api/items/', include(('hardees.api.urls', 'items'), namespace='items-api')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
