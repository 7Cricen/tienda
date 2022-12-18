from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
  lista_display = ['nombre', 'slug']
  prepopulated_fields = {'slug': ('nombre',)}
  # el campo slug se completa automaticamente de nombre

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'autor', 'slug', 'precio', 'en_stock', 'creado', 'actualizado']
  list_filter = ['en_stock', 'activo']
  list_editable = ['precio', 'en_stock']
  prepopulated_fields = {'slug': ('titulo',)}
  # el campo slug se completa automaticamente de titulo

# Respetar los nombres en ingles de las variables o no los reconoce