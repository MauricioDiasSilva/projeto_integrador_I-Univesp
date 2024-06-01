from django.db import models

class CriancaEspecial(models.Model):
    nome = models.CharField(max_length=100, null=True, default="Insira seu Nome")
    idade = models.PositiveIntegerField(null=True, default=None)
    descricao = models.TextField(null=True, default="Insira a descrição da necessidade")
    responsavel = models.CharField(max_length=100, null=True, default="Insira um Nome")
    endereco = models.CharField(max_length=200, null=True, default="Insira um endereço")
    telefone = models.CharField(max_length=80, null=True, default="Insira um telefone")
    email = models.EmailField(
        max_length=200, null=True, default="seunome@instituição.com.br")

    def __str__(self):
        return self.nome
    
class Missao(models.Model):
    titulo = models.CharField(max_length=200, null=True, default="Insira um Título")
    texto = models.TextField(null=True, default="Insira um texto")
    imagem = models.ImageField(upload_to='static/imagens', null=True)
    descricao_imagem = models.CharField(max_length=200, null=True, default="Insira a descrição da necessidade")

class ValorImage(models.Model):
    imagem = models.ImageField(upload_to='static/imagens', null=True)
    # outros campos, se necessário

class Contato(models.Model):
    nome = models.CharField(max_length=200, null=True, default="Insira seu Nome")
    email = models.EmailField(null=True, default="Insira seu Email")
    telefone = models.CharField(max_length=20, null=True, default="Insira um telefone")
    observacoes = models.TextField(null=True, default='Sem observações')



