# myapp/forms.py

from django import forms
from .models import CriancaEspecial
from django.contrib.auth.models import User


class CriancaEspecialForm(forms.ModelForm):
    class Meta:
        model = CriancaEspecial
        # Inclua apenas os campos essenciais
        fields = ['nome', 'telefone', 'email']


class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(CadastroForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
