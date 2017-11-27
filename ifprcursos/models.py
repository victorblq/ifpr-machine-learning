# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models

# Create your models here.
class Resposta(models.Model):
    id = models.AutoField(primary_key=True)
    respostas = models.CommaSeparatedIntegerField(max_length=255, null=True)
    curso = models.IntegerField('curso', null=True)

class Pergunta(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % (self.titulo)

class Alternativa(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=150, default="erro")
    valor = models.IntegerField('valor')
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, default="erro")
    valor = models.IntegerField('valor')
    
    def __unicode__(self):
        return u"%s" % (self.nome)