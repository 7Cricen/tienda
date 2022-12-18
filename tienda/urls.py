from django.urls import path
from . import views

app_name = 'tienda' # Respetar nombre en ingles de la variable

urlpatterns = [
    path('', views.productos_all, name='productos_all'),
    path('item/<slug:slug>/', views.producto_detalles, name='producto_detalles'),
    path('categoria/<slug:categoria_slug>/', views.categoria_lista, name='categoria_lista'),
]
