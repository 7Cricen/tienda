from tienda.models import Producto
from decimal import Decimal

class Carrito():

  def __init__(self, request):
    self.session = request.session
    carrito = self.session.get('skey')

    if 'skey' not in request.session:
      carrito = self.session['skey'] = {}

    self.carrito = carrito

  def agregar(self, producto, cantidad):
    producto_id = str(producto.id)

    if producto_id in self.carrito:
      self.carrito[producto_id]['cantidad'] = cantidad
    else:
      self.carrito[producto_id] = {'precio': str(producto.precio), 'cantidad': int(cantidad)}
    
    self.guardar()

  def __iter__(self):
    producto_ids = self.carrito.keys()
    productos = Producto.producto.filter(id__in=producto_ids)
    carrito = self.carrito.copy()

    for x in productos:
      carrito[str(x.id)]['producto'] = x

    for item in carrito.values():
      item['precio'] = Decimal(item['precio'])
      item['precio_total'] = item['precio'] * item['cantidad']
      yield item
  
  def __len__(self):
    return sum(item['cantidad'] for item in self.carrito.values())

  def get_precio_total(self):
    return sum(Decimal(item['precio']) * (item['cantidad']) for item in self.carrito.values())

  def eliminar(self, producto):
    producto_id = str(producto)
    if producto_id in self.carrito:
      del self.carrito[producto_id]
      
      self.guardar()  
      
  def actualizar(self, producto, cantidad):
    producto_id = str(producto)

    if producto_id in self.carrito:
      self.carrito[producto_id]['cantidad'] = cantidad
      
    self.guardar()

  def guardar(self):
    self.session.modified = True
