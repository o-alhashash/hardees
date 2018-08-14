from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from hardees.views import ItemListView, ItemDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', ItemListView.as_view(), name='items'),
    path('items/<slug:pk>/', ItemDetailView.as_view(), name='item-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
