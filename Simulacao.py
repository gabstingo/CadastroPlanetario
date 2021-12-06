import math
import os
from operator import itemgetter
from Calculos import Calculos

class Simulacao():

    def __init__(self):
        self.__calculos = None
        self.__tempoSimulacao = None
        self.__granulosidade = None
        self.__categorias = None
        self.__texto = ''

    @property
    def texto(self):
        return self.__texto

    def insereAtributos(self, calculos, tempoSimulacao, granulosidade, categorias):
        self.__calculos = calculos
        self.__tempoSimulacao = tempoSimulacao
        self.__granulosidade = granulosidade
        self.__categorias = categorias

    def executaSimulacao(self):
        passos = math.ceil(self.__tempoSimulacao/self.__granulosidade)
        texto = ''
        for i in range(0, passos+1):
            texto += ('-=' * 25)
            if(i == 0):
                texto += " Inicio da Simulacao "
            else:
                texto += " Simulacao {} ".format(i)

            texto += ('-=' * 25)
            texto += "\n"
            texto += self.__calculos.mostraCorpos(self.__categorias, passos, i)
        
            texto += "\nCalculos: \n"       
            texto += "\nMedia das distancias: {}\n".format(self.__calculos.mediaDistancia(passos, i))
            texto += "\nMedia das massas: {}".format(self.__calculos.mediaMassas())
            texto += "\nDesvio padrao das massas: {}".format(self.__calculos.desvioPadrao())
            texto += "\n\nForça gravitacional resultante: \n"
            texto += self.__calculos.calculoForcaGravitacional(passos, i)
            texto += "\n\n"
        
        self.__texto = texto
        return self.__texto
    
    def salvar(self, nomeArquivo):
        arquivo = open(nomeArquivo, "w")
        arquivo.write(self.__texto)
        arquivo.close()
        