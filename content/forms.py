from django import forms
from content.models import *
from datetime import datetime
from djangoProject.settings import DATETIME_INPUT_FORMATS

class ZayavkiForm(forms.ModelForm):
    class Meta:
        model = Zayavki
        fields = '__all__'
        widgets = {
            'name_klient': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'telephon': forms.TextInput(
                attrs={'type': 'tel', 'class': 'form-control', 'placeholder': 'Номер телефона'}),
            'pricheski': forms.Select(attrs={'class': 'form-select'}),
            'makeup': forms.Select(attrs={'class': 'form-select'}),
            'vizajist': forms.Select(attrs={'class': 'form-select'}),
            'data_vypoln': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата и время'})
        }


class VizajisForm(forms.ModelForm):
    class Meta:
        model = Vizajisti
        fields = '__all__'
        widgets = {
            'fam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'kvalifikaciya': forms.Select(attrs={'class': 'form-select'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'})
        }


class MakeupForm(forms.ModelForm):
    class Meta:
        model = Makeup
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'opisanie': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'stoimost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Стоимость'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'})
        }


class PricheskiForm(forms.ModelForm):
    class Meta:
        model = Pricheski
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'opisanie': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'stoimost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Стоимость'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'})
        }


class KvalifikaciyaForm(forms.ModelForm):
    class Meta:
        model = Kvalifikaciya
        fields = '__all__'
        widgets = {
            'opyt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Опыт'}),
            'procent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Надбавка'}),
        }
