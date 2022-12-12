from django import forms
from .models import UsuarioBase
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm, SetPasswordForm)


class UsuarioLoginForm(AuthenticationForm):
  # username respetar el nombre en ingles
  username = forms.CharField(label='E-mail',widget=forms.TextInput(
      attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'login-username'}))
  password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
      attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'id': 'login-pwd'}
  ))


class RegistroForm(forms.ModelForm):
  
  nombre_usuario = forms.CharField(label='Nombre de Usuario', max_length=50, min_length=4, help_text='Requerido')
  email = forms.EmailField(max_length=100, help_text='Requerido', error_messages={'requerido': 'Necesitas un email'})
  password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

  class Meta:
    model = UsuarioBase
    fields = ('nombre_usuario', 'email')

  def clean_user_name(self):
    nombre_usuario = self.cleaned_data['nombre_usuario'].lower()
    r = UsuarioBase.objects.filter(nombre_usuario=nombre_usuario)
    if r.count():
      print('raise hijo de puta')
      raise forms.ValidationError("El nombre de usuario ya existe")
    return nombre_usuario

  def limpiar_password(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError("Las contraseñas no coinciden")
    return cd['password2']

  def limpiar_email(self):
    email = self.cleaned_data['email']
    x = UsuarioBase.objects.filter(email=email)
    if x.exists():
      raise forms.ValidationError('El email ya esta en uso')
    return email

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['nombre_usuario'].widget.attrs.update(
      {'class': 'form-control mb-3', 'placeholder': 'Nombre de usuario'}
    )
    self.fields['email'].widget.attrs.update(
      {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'form-control mb-3', 'placeholder': 'Contraseña'}
    )
    self.fields['password2'].widget.attrs.update(
      {'class': 'form-control', 'placeholder': 'Repetir Contraseña'}
    )


class EditarUsuarioForm(forms.ModelForm):

  email = forms.EmailField(label='E-mail (no se puede cambiar)', max_length=200, 
    widget=forms.TextInput(
      attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email', 'readonly': 'readonly'}))

  nombre_usuario = forms.CharField(label='Nombre de Usuario', min_length=4, max_length=50,
    widget=forms.TextInput(
      attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre de Usuario', 'id': 'form-firstname', 'readonly': 'readonly'}))

  nombre = forms.CharField(label='Nombre', min_length=4, max_length=50, 
    widget=forms.TextInput(
      attrs={'class': 'form-control mb-3', 'placeholder': 'Nombre', 'id': 'form-lastname'}))

  class Meta:
    model = UsuarioBase
    fields = ('email', 'nombre_usuario', 'nombre',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['nombre_usuario'].required = True
    self.fields['email'].required = True


class PasswordReiniciarForm(PasswordResetForm):

  email = forms.EmailField(max_length=254, label='E-mail',
    widget=forms.TextInput(
      attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))

  def limpiar_email(self):
    email = self.cleaned_data['email']
    u = UsuarioBase.objetos.filter(email=email)
    if not u:
      raise forms.ValidationError(
        'Desafortunadamente no se ha podido encontrar el E-mail')
    return email


class PasswordReiniciarConfirmacionForm(SetPasswordForm):
  # new_password1 y new_password2 respetar el nombre en ingles
  new_password1 = forms.CharField(label='Nueva Contraseña', 
  widget=forms.PasswordInput(
    attrs={'class': 'form-control mb-3', 'placeholder': 'Nueva Contraseña', 'id': 'form-newpass'}))

  new_password2 = forms.CharField(label='Repetir Contraseña', 
  widget=forms.PasswordInput(
    attrs={'class': 'form-control mb-3', 'placeholder': 'Repetir Contraseña', 'id': 'form-new-pass2'}))