from django.shortcuts import render, redirect
from .models import Missao, ValorImage
from .forms import ContatoForm  # Adicione esta linha
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/admin')  # Redireciona para a página de administração
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
    else:
        return render(request, 'login.html')


def index(request):
    return render(request, 'siteweb/index.html')



def doacao(request):
    return render(request, 'siteweb/doacao.html')

def missao(request):
    missoes = Missao.objects.all()
    return render(request,'siteweb/missao.html', {'missoes': missoes} )

def valores(request):
    imagens = ValorImage.objects.all()
    return render(request, 'siteweb/valores.html', {'imagens': imagens})

def cadastro(request):

  if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/admin')  # Redireciona para a página de administração
        else:
            return render(request, 'siteweb/cadastro.html', {'error': 'Usuário ou senha inválidos'})
  else:
        return render(request, 'siteweb/cadastro.html')
    
def base(request):
    return render(request, 'siteweb/base.html')

        
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContatoForm()

    return render(request, 'siteweb/contato.html', {'form': form})










     