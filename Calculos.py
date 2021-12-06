import math
import os
from operator import itemgetter
from CorpoCeleste import CorpoCeleste

class Calculos:

    def __init__(self):
        self.__corpos = []
        self.__distancias = None
        self.__massas = None
        self.__desvioPadrao = None

    @property
    def corpos(self):
        return self.__corpos

    def insereCorpo(self, corpo):
        inserido = False
        for indice, valor in enumerate(self.__corpos):
            if(corpo.massa > valor.massa):
                self.__corpos.insert(indice, corpo)
                inserido = True
                break
        if(inserido == False):
            self.__corpos.append(corpo)

    def existeCorpo(self, nomeBusca):
        achou = False
        for i in range(0, len(self.__corpos)):
            if(self.__corpos[i].nomeCorpo == nomeBusca):
                achou = True

        return achou


    def mediaDistancia(self, passos, simulacao):
        self.__distancias = 0
        #calcula a distancia baseana na quantidade
        '''
        Exemplo: a saida abaixo realiza o calculo da seguinte maneira
            corpos[0] com corpos[1]
            corpos[0] com corpos[2]
            corpos[2] com corpos[1]
        '''
        for i in range(0, len(self.__corpos)):
            if(0 <= i < len(self.__corpos)-1):
                for j in range(0, len(self.__corpos)):
                    if(j > i):
                        self.__distancias += self.__corpos[i].distanciaCorpo(self.__corpos[j], passos, simulacao)
        if(len(self.__corpos) > 0):
            return (self.__distancias / (len(self.__corpos)))            
        else:
            return self.__distancias            

    def mediaMassas(self):
        self.__massas = 0
        for i in range(0, len(self.__corpos)):
            self.__massas += self.__corpos[i].massa
        
        if(len(self.__corpos) > 0):
            self.__massas = self.__massas / len(self.__corpos)

        return self.__massas

    def desvioPadrao(self):
        self.__desvioPadrao = 0
        #dp = raiz(soma(m[i] - médiaDasMassas)) / qtdCorpos)
        for i in range(0, len(self.__corpos)):
            #eleva as massas subtraidas da média ao quadrado
            self.__desvioPadrao += pow((self.__corpos[i].massa - self.__massas), 2)

        #divide os valores pela quantidade de massas
        if(len(self.__corpos) > 0):
            self.__desvioPadrao = self.__desvioPadrao / len(self.__corpos) 
        else:
            self.__desvioPadrao

        # retorna a raiz da somatoria com arredondamento de duas casas após a virgula
        return round(math.sqrt(self.__desvioPadrao), 2)
        
    def calculoForcaGravitacional(self, passos, simulacao):
        texto = ''
        for i in range(0, len(self.__corpos)):
            if(0 <= i < len(self.__corpos)-1):
                for j in range(0, len(self.__corpos)):
                    if(j > i):
                        texto += "Força gravitacional de {} a {} resulta em {}\n".format(self.__corpos[i].nomeCorpo, self.__corpos[j].nomeCorpo,self.__corpos[i].forcaGravitacional(self.__corpos[j], passos, simulacao))
        
        return texto

    def mostraCorpos(self, categorias, passos, simulacao):
        texto = ''
        for categoria in categorias:
            texto += categoria
            for i in range(0, len(self.__corpos)):
                if(self.__corpos[i].categoria == categoria):
                    texto += "\n\tNome do Corpo: {}, ".format(self.__corpos[i].nomeCorpo)
                    texto += "Massa: {}, ".format(self.__corpos[i].massa)
                    texto += "Coordenada X inicial/final: {}/{}, ".format((self.__corpos[i].x0 + self.__corpos[i].translacaoX(passos, simulacao)), self.__corpos[i].x1)
                    texto += "Coordenada Y inicial/final: {}/{}, ".format((self.__corpos[i].y0 + self.__corpos[i].translacaoY(passos, simulacao)), self.__corpos[i].y1)
                    texto += "Coordenada Z inicial/final: {}/{}".format((self.__corpos[i].z0 + self.__corpos[i].translacaoZ(passos, simulacao)), self.__corpos[i].z1)
                    
            texto += "\n"
            texto += ('-=' * 60)
            texto += "\n"
        return texto
    
