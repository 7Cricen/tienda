from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy
from django.core.mail import send_mail

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class AdministradorCuentas(BaseUserManager):
  def create_superuser(self, email, nombre_usuario, password, **other_fields):

    other_fields.setdefault('is_staff', True)
    other_fields.setdefault('is_superuser', True)
    other_fields.setdefault('is_active', True)

    if other_fields.get('is_staff') is not True:
      raise ValueError('El superusuario debe estar asignado a is_staff=True.')
      
    if other_fields.get('is_superuser') is not True:
      raise ValueError('El superusuario debe estar asignado a is_superuser=True.')

    return self.create_user(email, nombre_usuario, password, **other_fields)

  def create_user(self, email, nombre_usuario, password, **other_fields):
      if not email:
        raise ValueError(gettext_lazy('Debes proporcionar una dirección de correo electrónico'))

      email = self.normalize_email(email)
      usuario = self.model(email=email,  nombre_usuario=nombre_usuario,**other_fields)
      usuario.set_password(password)
      usuario.save()
      return usuario

class UsuarioBase(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(gettext_lazy('direccion email'), unique=True)
  nombre_usuario = models.CharField(max_length=150, unique=True)
  nombre = models.CharField(max_length=150, blank=True)
  apellido = models.CharField(max_length=150, blank=True)
  pais = CountryField()
  provincia = models.CharField(max_length=150, blank=True)
  numero_telefono = models.CharField(max_length=15, blank=True)
  codigo_postal = models.CharField(max_length=12, blank=True)
  direccion = models.CharField(max_length=150, blank=True)
  nota = models.TextField(gettext_lazy('acerca_de'), max_length=500, blank=True)

  # is_active respetar el nombre en ingles
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  creado = models.DateTimeField(auto_now_add=True)
  actualizado = models.DateTimeField(auto_now=True)

  objetos = AdministradorCuentas()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['nombre_usuario']
  
  def email_usuario(self, asunto, mensaje):
    send_mail(
        asunto,
        mensaje,
        'l@1.com',
        [self.email],
        fail_silently=False,
    )

  class Meta:
    verbose_name = 'Cuentas'
    verbose_name_plural = 'Cuentas'

  def __str__(self):
    return self.nombre_usuario