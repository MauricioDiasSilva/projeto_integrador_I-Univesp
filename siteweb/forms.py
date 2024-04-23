# myapp/forms.py

from django import forms
from .models import CriancaEspecial


class CriancaEspecialForm(forms.ModelForm):
    class Meta:
        model = CriancaEspecial
        # Inclua apenas os campos essenciais
        fields = ['nome', 'telefone', 'email']
