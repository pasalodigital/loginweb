from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import Input, PasswordInput


class RegistrarUsuarioForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
            'first_name': Input(attrs={'placeholder': 'Nombre'}),
            'last_name': Input(attrs={'placeholder': 'Apellido'}),
            'username': Input(attrs={'placeholder': 'Usuario'}),
            'email': Input(attrs={'placeholder': 'Correo'}),
            'password': PasswordInput(attrs={'placeholder': 'Contrasena'})
        }


class LoginUsuarioForm(forms.Form):

    username = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(required=True, max_length=15, widget=forms.PasswordInput)

    def get_data(self):

        return User.objects.get(username=self.cleaned_data['user'], password=self.cleaned_data['password'])
