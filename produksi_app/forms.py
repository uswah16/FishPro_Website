from django.forms import ModelForm
from django import forms
from produksi_app.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormPerikanan(ModelForm):
    class Meta:
        model = Perikanan
        fields = '__all__'
       

        widgets = {
            'Jenis_Ikan' : forms.TextInput({'class': 'form-control', 'placeholder' : 'Jenis Ikan'}),
            'Jenis_Usaha' : forms.TextInput({'class': 'form-control', 'placeholder' : 'Jenis Usaha'}),
            'Tahun' : forms.NumberInput({'class': 'form-control', 'placeholder' : 'tahun'}),
            'Volume_Produksi' : forms.TextInput({'class': 'form-control', 'placeholder' : 'Volume Produksi'}),
            'Nilai_Produksi' : forms.TextInput({'class': 'form-control', 'placeholder' : 'Nilai Produksi'}),
            'img' : forms.TextInput({'class': 'form-control', 'placeholder' : 'Image'}),
            'Provinsi' : forms.Select({'class': 'form-control', 'placeholder' : 'Provinsi'}),
            'Detail' : forms.URLInput({'class': 'form-control', 'placeholder' : 'Detail'}),

        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']