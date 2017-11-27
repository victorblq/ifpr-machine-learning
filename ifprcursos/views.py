# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn import tree

from serializers import RespostaSerializer, PerguntaSerializer, AlternativaSerializer, CursoSerializer
from models import Resposta, Pergunta, Alternativa, Curso

# Create your views here.
class RespostaViewSet(viewsets.ModelViewSet):
    """
    API endpoint for respostas
    """
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer

class PerguntaViewSet(viewsets.ModelViewSet):
    """
    API endpoint for perguntas
    """
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

class AlternativaViewSet(viewsets.ModelViewSet):
    """
    API endpoint for alternativas
    """
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint for cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

@api_view(['POST'])
def predict(request):
    resposta = Resposta(respostas=request.data)
    
    respostasSalvas = Resposta.objects.all()
    
    dadosTreino = []
    marcacoesTreino = []
    
    for respostaSalva in respostasSalvas:
        respostaSalva.respostas = respostaSalva.respostas\
            .replace("[", "").replace("]", "").replace("u", "").replace("'", "")
        
        dadosResposta = []
        
        for valorResposta in respostaSalva.respostas.split(","):
            dadosResposta.append(int(valorResposta))        
        
        dadosTreino.append(dadosResposta)
        
        marcacoesTreino.append(respostaSalva.curso)
        
    classificador = tree.DecisionTreeClassifier()
    classificador = classificador.fit(dadosTreino, marcacoesTreino)
    
    dadosTeste = [request.data]
    resultado = classificador.predict(dadosTeste)

    resposta.curso = resultado
    respostasToInt = []

    for respostaToInt in resposta.respostas:
        respostasToInt.append(int(respostaToInt))

    resposta.respostas = respostasToInt

    resposta.save()

    curso = Curso.objects.get(pk=resposta.curso)

    serializer = CursoSerializer(curso)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def home(request):
    return render(request, 'index.html')
