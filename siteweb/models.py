
from django.db import models


class CriancaEspecial(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    descricao = models.TextField()
    responsavel = models.CharField(max_length=100, default="Insira um Nome")
    endereço = models.CharField(max_length=200, default="Insira um endereço")
    telefone = models.CharField(max_length=80, default="Insira um telefone")

    def __str__(self):
        return self.nome
