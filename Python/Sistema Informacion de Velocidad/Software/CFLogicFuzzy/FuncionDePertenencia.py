# -*- coding: utf-8 -*-
import math


class FuncionPertenencia:

    def __init__(self,valor,tipo,coordenadas):
        self.valor = float(valor)
        self.tipo = tipo
        self.coordenadas = coordenadas

    def determinarFuncion(self):
        if self.tipo == "Trapezoidal":
            return Trapezoidal(self.valor,self.coordenadas)

        if self.tipo == "Triangular":
            return Triangular(self.valor,self.coordenadas)

        if self.tipo == "Singleton":
            return Singleton(self.valor,self.coordenadas)

        if self.tipo == "Gausiana":
            return Gausiana(self.valor,self.coordenadas)

        if self.tipo == "Campana":
            return Campana(self.valor,self.coordenadas)

        if self.tipo == "Sigmoide":
            return Sigmoide(self.valor,self.coordenadas)


class Trapezoidal:

    def __init__(self,valor,coordenadas):
        self.valor = valor
        self.a,self.b,self.c,self.d = coordenadas
        self.vp = 0

    def calcular(self):
        if self.valor < self.a:
            self.vp = 0
            return self.vp

        if self.a <= self.valor <= self.b:
            self.vp = (self.valor - self.a) / (self.b - self.a)
            return self.vp

        if self.b <= self.valor <= self.c:
            self.vp = 1
            return self.vp

        if self.c <= self.valor <= self.d:
            self.vp = (self.d - self.valor) / (self.d - self.c)
            return self.vp

        if self.valor > self.d:
            self.vp = 0
            return self.vp


class Trapezoidal_Derecho:

    def __init__(self,valor,coordenadas):
        self.valor = valor
        self.a,self.b = coordenadas
        self.vp = 0

    def calcular(self):
        if self.valor < self.a:
            self.vp = 0
            return self.vp

        if self.a <= self.valor <= self.b:
            self.vp = (self.valor - self.a) / (self.b - self.a)
            return self.vp

        if self.valor > self.b:
            self.vp = 1
            return self.vp


class Trapezoidal_Izquierdo:

    def __init__(self,valor,coordenadas):
        self.valor = valor
        self.a,self.b = coordenadas
        self.vp = 0

    def calcular(self):
        if self.valor < self.a:
            self.vp = 1
            return self.vp

        if self.a <= self.valor <= self.b:
            self.vp = (self.b-self.valor) / (self.b - self.a)
            return self.vp

        if self.valor > self.b:
            self.vp = 0
            return self.vp


class Triangular:

    def __init__(self,valor,coordenadas):
        self.valor = valor
        self.a,self.b,self.c = coordenadas
        self.vp = 0

    def calcular(self):
        if self.valor < self.a:
            self.vp = 0
            return self.vp

        if self.a <= self.valor <= self.b:
            self.vp = (self.valor - self.a) / (self.b - self.a)
            return self.vp

        if self.b <= self.valor <= self.c:
            self.vp = (self.c - self.valor) / (self.c - self.b)
            return self.vp

        if self.valor > self.c:
            self.vp = 0
            return self.vp


class Singleton:

    def __init__(self,valor,coordenadas):
        self.valor = valor
        self.a = coordenadas
        self.vp = 0

    def calcular(self):

        if self.valor == self.a:
            self.vp = 1
            return self.vp

        else:
            self.valor = 0
            return self.vp


class Gausiana:

    def __init__(self,valor,coordenadas):
        self.valor = valor
        self.a, self.b = coordenadas
        self.vp = 0

    def calcular(self):
        self.vp = math.exp((-1/2)*(((self.valor-self.a)/self.b)**2))
        return self.vp


class Campana:

    def __init__(self,valor,coordenadas):
        self.valor = valor
        self.a,self.b,self.c = coordenadas
        self.vp = 0

    def calcular(self):
        self.vp = 1 / (1 + (abs((self.valor - self.c) / self.a)**(2 * self.b)))
        return self.vp


class Sigmoide:

    def __init__(self,valor,coordenadas):
        self.valor = valor
        self.a,self.b = coordenadas
        self.vp = 0

    def calcular(self):
        self.vp = 1 / (1 + math.exp(-self.a * (self.valor - self.b)))
        return self.vp

