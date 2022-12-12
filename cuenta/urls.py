from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .forms import (UsuarioLoginForm, PasswordReiniciarForm, PasswordReiniciarConfirmacionForm)
from . import views

app_name = 'cuenta'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(
    template_name='cuenta/registro/login.html', 
    form_class=UsuarioLoginForm), 
    name='login'),

  path('logout/', auth_views.LogoutView.as_view(
    next_page='/cuenta/login/'), 
    name='logout'),

  path('registrar/', views.registrar_cuenta, name='registrar'),

  path('activar/<slug:uidb64>/<slug:token>', views.activar_cuenta, name='activar'),

  path('reiniciar_password/', auth_views.PasswordResetView.as_view (
    template_name='cuenta/usuario/reiniciar_password.html', 
    success_url='reiniciar_password_confirmacion_email', #1
    email_template_name='cuenta/usuario/reiniciar_password_email.html',
    form_class=PasswordReiniciarForm),
    name='reiniciar_password'),
  #1
  path('reiniciar_password/reiniciar_password_confirmacion_email/', TemplateView.as_view(
    template_name="cuenta/usuario/reiniciar_estado.html"), 
    name='reiniciar_password_hecho'),

  path('reiniciar_password_confirmacion/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
  template_name='cuenta/usuario/reiniciar_password_confirmacion.html', 
  success_url='/cuenta/reiniciar_password_completo/', #2
  form_class=PasswordReiniciarConfirmacionForm),
  name="reiniciar_password_confirmacion"),
  #2
  path('reiniciar_password_completo/', TemplateView.as_view(template_name="cuenta/usuario/reiniciar_estado.html"), name='reiniciar_password_completo'),

  # Panel de control del usuario
  path('control_panel/', views.control_panel, name='control_panel'),

  path('perfil/editar/', views.editar_detalles, name='editar_detalles'),

  path('perfil/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),

  path('perfil/eliminar_confirmacion/', TemplateView.as_view(
    template_name='cuenta/usuario/eliminar_confirmacion.html'), 
    name='eliminar_confirmacion'),
]