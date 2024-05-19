
from django.db import models

class CriancaEspecial(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    descricao = models.TextField()
    responsavel = models.CharField(max_length=100, default="Insira um Nome")
    endereço = models.CharField(max_length=200, default="Insira um endereço")
    telefone = models.CharField(max_length=80, default="Insira um telefone")
    email = models.EmailField(
        max_length=200, default="seunome@instituição.com.br")

    def __str__(self):
        return self.nome
    
class Missao(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='static/imagens')
    

class ValorImage(models.Model):
    imagem = models.ImageField(upload_to='static/imagens')
    # outros campos, se necessário

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    Observacoes = models.TextField(default='Sem observações')





