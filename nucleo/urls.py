from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls', namespace='tienda')),
    path('carrito/', include('carrito.urls', namespace='carrito')),
    path('cuenta/', include('cuenta.urls', namespace='cuenta')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)