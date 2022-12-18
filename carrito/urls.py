from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.carrito_resumen, name='carrito_resumen'),
    path('agregar/', views.carrito_agregar, name='carrito_agregar'),
    path('eliminar/', views.carrito_eliminar, name='carrito_eliminar'),
    path('actualizar/', views.carrito_actualizar, name='carrito_actualizar'),
]
