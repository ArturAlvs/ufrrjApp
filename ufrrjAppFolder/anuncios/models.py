from django.db import models

# Create your models here.

import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)




class Anunciante(models.Model):
    matricula = models.PositiveIntegerField(unique=True)
    senha = models.CharField(max_length=16) #hash
    salt = models.PositiveIntegerField()

    nome = models.CharField(max_length=20)
    foto = models.CharField(max_length=200) #o caminho da imagem

    telefone = models.CharField(max_length=20)

    tem_troco = models.BooleanField()
    tem_cartao = models.BooleanField()

class Produto(models.Model):
    nome = models.CharField(max_length=20)
    preco = models.FloatField()
    foto_prod = models.CharField(max_length=200) #o caminho da imagem

    anunciante_prod = models.ForeignKey(Anunciante, on_delete=models.CASCADE)

class Horario(models.Model):

    anunciante_horario = models.OneToOneField(Anunciante, on_delete=models.CASCADE, primary_key=True)

    segunda = models.CharField(max_length=140)
    terca = models.CharField(max_length=140)
    quarta = models.CharField(max_length=140)
    quinta = models.CharField(max_length=140)
    sexta = models.CharField(max_length=140)