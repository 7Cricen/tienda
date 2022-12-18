from django.shortcuts import render, get_object_or_404
from .carrito import Carrito
from tienda.models import Producto
from django.http import JsonResponse

def carrito_resumen(request):
  carrito = Carrito(request)
  return render(request, 'carrito/resumen.html', {'carrito':carrito})

def carrito_agregar(request):
  carrito = Carrito(request)
  if request.POST.get('action') == 'post':
    producto_id = int(request.POST.get('productoid'))
    producto_cantidad = int(request.POST.get('productocantidad'))
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.agregar(producto=producto, cantidad=producto_cantidad)

    carrito_cantidad = carrito.__len__()
    respuesta = JsonResponse({'cantidad':carrito_cantidad})
    return respuesta

def carrito_eliminar(request):
  carrito = Carrito(request)
  if request.POST.get('action') == 'post':
    producto_id = int(request.POST.get('productoid'))
    carrito.eliminar(producto=producto_id)

    carrito_cantidad = carrito.__len__()
    carrito_total = carrito.get_precio_total()
    
    respuesta = JsonResponse({'cantidad':carrito_cantidad, 'subtotal':carrito_total})
    return respuesta

def carrito_actualizar(request):
  carrito = Carrito(request)
  if request.POST.get('action') == 'post':
    producto_id = int(request.POST.get('productoid'))
    producto_cantidad = int(request.POST.get('productocantidad'))
    carrito.actualizar(producto=producto_id, cantidad=producto_cantidad)

    carrito_cantidad = carrito.__len__()
    carrito_total = carrito.get_precio_total()
    
    respuesta = JsonResponse({'cantidad':carrito_cantidad, 'subtotal':carrito_total})
    return respuesta