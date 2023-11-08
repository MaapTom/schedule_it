from django import forms
from .widgets import CPFFormatWidget
from .widgets import PhoneFormatWidget
from .models import Collaborator
# Importe a classe Scheduling do seu arquivo models.py
from .models import Scheduling
from django.forms.widgets import DateInput

class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = '__all__'
        widgets = {
            'cpf': CPFFormatWidget(),
        }


class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = '__all__'
        widgets = {
            'phone': PhoneFormatWidget(),
        }


class SchedulingForm(forms.ModelForm):
    class Meta:
        model = Scheduling
        fields = ['collaborator', 'day', 'hours','service']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'})
        }
