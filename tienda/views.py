from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto


def productos_all(request):
  productos = Producto.producto.all() # Toma todos los productos de la base de datos
  return render(request, 'tienda/home.html', {'productos': productos})

def producto_detalles(request, slug):
  producto = get_object_or_404(Producto, slug=slug, en_stock=True)
  return render(request, 'tienda/productos/producto.html', {'producto': producto})

def categoria_lista(request, categoria_slug):
  categoria = get_object_or_404(Categoria, slug=categoria_slug)
  productos = Producto.objects.filter(categoria=categoria)
  return render(request, 'tienda/productos/categoria.html', {'categoria': categoria, 'productos': productos})

