# ARQUIVO VIEWS
from django.shortcuts import render, redirect
from .forms import CriancaEspecialForm
from .forms import CadastroForm



def index(request):
    return render(request, 'siteweb/index.html')


def contato(request):
    return render(request, 'siteweb/contato.html')


def missao(request):
    return render(request, 'siteweb/missao.html')


def valores(request):
    return render(request, 'siteweb/valores.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CadastroForm()
    return render(request, 'siteweb/cadastro.html', {'form': form})


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

    return render(request, 'contato.html', {'form': form})




     