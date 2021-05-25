from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import HiddenInput

from .models import Perfil, Oferta, Candidatura


class DateInput(forms.DateInput):
    input_type='date'
class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput(
        attrs={
            'class':'form-control',
            'required':'required',
            'pattern':'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*_=+-]).{8,12}$',
            'title':'La contraseña debe contener 1 Mayuscula 1 Minúscula 1 Número 1 Símbolo !@#$%^&*_=+- y entre 8 y 20 carácteres',
        }
    ))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'required':'required',
            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*_=+-]).{8,12}$',
            'title': '1 Mayuscula 1 Minúscula 1 Número 1 Símbolo !@#$%^&*_=+- y entre 8 y 20 carácteres',
        }
    ))

    class Meta:
        model = Perfil
        fields = [
            'username',
            'email',
            'nombre',
            'apellidos',
            'foto',
            'fecha_nacimiento',
            'cvc',
            'telf_usuario'
        ]
        widgets = {
            'username':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'pattern':'^[a-zA-Z0-9\s!@#$%^&*()]+$',
                    'title':'Nombre de usuario incorrecto',
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'title':'Email incorrecto',
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'pattern': '^[a-zA-Z0-9\s!@#$%^&*()]+$',
                    'title': 'Nombre incorrecto',
                }
            ),
            'apellidos':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'pattern':'^[a-zA-Z0-9\s!@#$%^&*()]+$',
                    'title':'Apellido/s incorrecto/s',
                }
            ),
            'foto':forms.FileInput(
                attrs={
                    'type':'file'
                }
            ),
            'fecha_nacimiento':DateInput(
                attrs={
                    'class':'form-control',
                    'required':'required'
                }
            ),
            'cvc':forms.FileInput(
                attrs={
                    'type':'file'

                }
            ),
            'telf_usuario':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'type':'tel',
                    'pattern':'^[6-9][0-9]{8}$',
                    'title':'Teléfono Incorrecto'
                }
            ),
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return password2
    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user

class FormOferta(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = [
            'titulo',
            'descripcion',
            'salario',
            'experiencia',
            'tipo_contrato',
        ]
        widgets={
            'titulo':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'pattern':'^[a-zA-Z0-9\s!@#$%^&*()]+$',
                    'title':'Has Intoducido Símbolos no Permitidos',
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'materialize-textarea',
                    'required':'required',
                    'pattern': '^[a-zA-Z0-9\s!@#$%^&*()]+$',
                    'title': 'Has Intoducido Símbolos no Permitidos',
                }
            ),
            'salario':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                }
            ),
            'experiencia':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'pattern': '^[a-zA-Z0-9\s!@#$%^&*()]+$',
                    'title': 'Has Intoducido Símbolos no Permitidos',
                }
            ),
            'tipo_contrato':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'pattern': '^[a-zA-Z0-9\s!@#$%^&*()]+$',
                    'title': 'Has Intoducido Símbolos no Permitidos',
                }
            )
        }
class FormCandidatura(forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = [
            'nombre_candidatura',
        ]
        widgets={
            'nombre_candidatura':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'required':'required',
                    'pattern': '^[a-zA-Z0-9\s!@#$%^&*()]+$',
                    'title': 'Has Intoducido Símbolos no Permitidos',
                }
            )
        }
