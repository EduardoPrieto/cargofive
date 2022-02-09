from django import forms
from .models import Contracts
from django.forms.widgets import ClearableFileInput, DateInput
from django.forms.widgets import TextInput, DateInput, FileInput
from datetime import datetime

today = datetime.today().strftime('%d-%m-%Y')

#Form para contrato, se añaden algunas validaciones aparte de las de fronEnd
#Se aplican las clases que llevaran los estilos
class NewContract(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = ['name', 'file', 'date']
        widgets = {
            'name': forms.DateInput(attrs={'class': 'form-control', 'type': 'text'}),
            'file': forms.FileInput(attrs={'accept':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel', 'class': 'form-control mt-2'}),
            'date': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'datepicker form-control', 'type': 'date', 'min': today})
        }

#Formulario para el filtro de Contratos
class FilterContract(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].required = False
    class Meta:
        model = Contracts
        fields = ['name', 'date']
        widgets = {
            'name': forms.DateInput(attrs={'class': 'form-control-sm', 'type': 'text', 'style':'outline: none'}),
            'date': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'datepicker form-control-sm', 'type': 'date','style':'outline: none'})
        }