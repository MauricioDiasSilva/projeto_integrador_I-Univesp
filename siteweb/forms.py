# myapp/forms.py

from django import forms
from .models import CriancaEspecial, Contato


class CriancaEspecialForm(forms.ModelForm):
    class Meta:
        model = CriancaEspecial
        # Inclua apenas os campos essenciais
        fields = ['nome', 'telefone', 'email', 'idade',]

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'observacoes']  # Use 'observacoes' aqui

