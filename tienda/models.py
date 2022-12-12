from django.db import models
from django.urls import reverse
from django.conf import settings

class Categoria(models.Model):
  nombre = models.CharField(max_length=255, db_index=True)
  slug = models.SlugField(max_length=255, unique=True)

  class Meta:
    verbose_name_plural = 'Categorias'

  def get_absolute_url(self):
      return reverse('tienda:categoria_lista', args=[self.slug])

  def __str__(self):
    return self.nombre


class ProductoManager(models.Manager):
  def get_queryset(self):
    return super(ProductoManager, self).get_queryset().filter(activo=True)


class Producto(models.Model):
  categoria = models.ForeignKey(Categoria, related_name='producto', on_delete=models.CASCADE)
  creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='producto_creador')
  titulo = models.CharField(max_length=255)
  autor = models.CharField(max_length=255, default='admin')
  descripcion = models.TextField(blank=True)
  imagen = models.ImageField(upload_to='images/', default='images/default.png')
  slug = models.SlugField(max_length=255)
  precio = models.DecimalField(max_digits=4, decimal_places=2)
  en_stock = models.BooleanField(default=True)
  activo = models.BooleanField(default=True)
  creado = models.DateTimeField(auto_now_add=True)
  actualizado = models.DateTimeField(auto_now=True)
  # objects = ProductoManager()
  objects = models.Manager()
  producto = ProductoManager()

  class Meta:
    verbose_name_plural = 'Productos'
    ordering = ('-creado',)

  def get_absolute_url(self):
      return reverse('tienda:producto_detalles', args=[self.slug])
  
  def __str__(self):
    return self.titulo