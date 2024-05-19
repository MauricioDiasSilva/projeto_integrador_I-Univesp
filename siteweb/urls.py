
# No seu arquivo urls.py
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as URLs do app 'meuapp'
    path('', views.index, name="index"),
    path('siteweb/missao.html', views.missao, name="missao"),
    path('siteweb/valores.html', views.valores, name="valores"),
    path('siteweb/cadastro.html', views.cadastro, name="cadastro"),
    path('siteweb/contato.html', views.contato, name="contato"),
    path('siteweb/doacao.html', views.doacao, name="doacao"),
]
