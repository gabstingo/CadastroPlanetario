import math
import os
from operator import itemgetter

class CorpoCeleste:

    def __init__(self, nomeCorpo, massa, x0, x1, y0, y1, z0, z1, categoria):
        self.__nomeCorpo = nomeCorpo
        self.__massa = massa
        self.__x0 = x0
        self.__x1 = x1
        self.__y0 = y0
        self.__y1 = y1
        self.__z0 = z0
        self.__z1 = z1
        self.__categoria = categoria

    @property
    def nomeCorpo(self):
        return self.__nomeCorpo

    @property
    def massa(self):
        return self.__massa

    @property
    def x0(self):
        return self.__x0

    @property
    def x1(self):
        return self.__x1

    @property
    def y0(self):
        return self.__y0

    @property
    def y1(self):
        return self.__y1

    @property
    def z0(self):
        return self.__z0

    @property
    def z1(self):
        return self.__z1

    @property
    def categoria(self):
        return self.__categoria

    def forcaGravitacional(self, corpo, passos, simulacao):
        constante = 6.67408 * pow(10, -11)
        distancia = pow(self.distanciaCorpo(corpo, passos, simulacao), 2)
        if(distancia != 0):
            return ((self.__massa * corpo.__massa) / distancia) * constante
        else:
            return 0


    def distanciaCorpo(self, corpo, passos, simulacao):
        # d = raiz((x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2)
        #obtem a distancias dos pontos ao quadrado
        distX = pow(((self.x0 + self.translacaoX(passos, simulacao)) - (corpo.x0 + corpo.translacaoX(passos, simulacao))), 2)
        distY = pow(((self.y0 + self.translacaoY(passos, simulacao)) - (corpo.y0 + corpo.translacaoY(passos, simulacao))), 2)
        distZ = pow(((self.z0 + self.translacaoZ(passos, simulacao)) - (corpo.z0 + corpo.translacaoZ(passos, simulacao))), 2)

        #arredonda a raiz para duas casas após a virgula
        return round(math.sqrt((distX+distY+distZ)), 2)

    def translacaoX(self, passos, simulacao):
        if(passos != 0 and simulacao > -1):
           return ((self.x1 - self.x0)/passos)*simulacao
        return 0
    
    def translacaoY(self, passos, simulacao):
        if(passos != 0 and simulacao > -1):
           return ((self.y1 - self.y0)/passos)*simulacao
        return 0
    
    def translacaoZ(self, passos, simulacao):
        if(passos != 0 and simulacao > -1):
           return ((self.z1 - self.z0)/passos)*simulacao
        return 0

    def editarCorpo(self, novaX0, novaX1, novaY0, novaY1, novaZ0, novaZ1):
        self.__x0 = novaX0
        self.__x1 = novaX1
        self.__y0 = novaY0
        self.__y1 = novaY1
        self.__z0 = novaZ0
        self.__z1 = novaZ1
