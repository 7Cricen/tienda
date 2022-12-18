from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import RegistroForm, EditarUsuarioForm
from .tokens import activar_token_cuenta
from .models import UsuarioBase


@login_required
def control_panel(request):
  return render(request, 'cuenta/usuario/control_panel.html')


@login_required
def editar_detalles(request):
  if request.method == 'POST':
    usuario_form = EditarUsuarioForm(instance=request.user, data=request.POST)

    if usuario_form.is_valid():
      usuario_form.save()

  else:
    usuario_form = EditarUsuarioForm(instance=request.user)

  return render(request,'cuenta/usuario/editar_detalles.html', {'usuario_form': usuario_form})


@login_required
def eliminar_usuario(request):
  usuario = UsuarioBase.objetos.get(nombre_usuario=request.user)
  usuario.is_active = False
  usuario.save()
  logout(request)
  return redirect('cuenta:eliminar_confirmacion')


def registrar_cuenta(request):
  if request.method == 'POST':
    registro_form = RegistroForm(request.POST)
    
    if registro_form.is_valid():
      print('valido')
      usuario = registro_form.save(commit=False)
      usuario.email = registro_form.cleaned_data['email']
      usuario.set_password(registro_form.cleaned_data['password'])
      usuario.is_active = False
      usuario.save()
      
      current_site = get_current_site(request)
      asunto = 'Activa tu cuenta'
      mensaje = render_to_string('cuenta/registro/email_activacion_cuenta.html',{
        'usuario': usuario,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(usuario.pk)),
        'token': activar_token_cuenta.make_token(usuario),
      })
      usuario.email_usuario(asunto=asunto, mensaje=mensaje)

    else:
      print('invalido')
  
  else:
    registro_form = RegistroForm()
  
  return render(request, 'cuenta/registro/registrar.html', {'form': registro_form})


def activar_cuenta(request, uidb64, token):
  try:
    uid = force_str(urlsafe_base64_decode(uidb64))
    usuario = UsuarioBase.objetos.get(pk=uid)

  except Exception as e:
    print(e)
    usuario = None

  if usuario is not None and activar_token_cuenta.check_token(usuario, token):
    usuario.is_active = True
    usuario.save()
    login(request, usuario)
    return redirect('cuenta:control_panel')

  else:
    return render(request, 'cuenta/registro/activacion_invalida.html')

