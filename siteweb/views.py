# ARQUIVO VIEWS
from django.shortcuts import render
# myapp/views.py

from .forms import CriancaEspecialForm


def index(request):
    return render(request, 'siteweb/index.html')


def contato(request):
    return render(request, 'siteweb/contato.html')


def missao(request):
    return render(request, 'siteweb/missao.html')


def valores(request):
    return render(request, 'siteweb/valores.html')


def cadastro(request):
    return render(request, 'siteweb/cadastro.html')


def base(request):
    return render(request, 'siteweb/base.html')


def minha_view(request):
    if request.method == 'POST':
        form = CriancaEspecialForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário e salvar no banco de dados
            form.save()
            # Redirecionar para uma página de sucesso ou outra página relevante
    else:
        form = CriancaEspecialForm()

    return render(request, 'cadastro.html', {'form': form})
