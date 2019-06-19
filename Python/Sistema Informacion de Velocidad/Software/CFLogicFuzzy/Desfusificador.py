# -*- coding: utf-8 *-*
"""
    -Obtener la forma geométrica obtenida de la inferencia
    -Crear la Clase Mandani y Clase del Japonés
    -Centroide por cada tipo de clase
    -Generar valor final
"""

class Desfusificador:

    def __init__(self,trapecio):
        self.trapecio = trapecio
        self.centroide = 0
        self.numerador = 0
        self.denominador = 0
        self.etiqueta = ""
        self.calcularCentroide()


    def calcularCentroide(self):

        self.etiqueta = ""

        for trap in self.trapecio:
            a,b,c,d,altura,etiqueta = trap
            if a==b:
                puntoMedio = (d-b)/2
                intervalo = d-b
                base = c-b
                Base = d-b
                area = ((Base-base) *altura)/2

            elif c==d:
                puntoMedio = (c-a)/2
                intervalo = c-a
                base = c-b
                Base = c-a
                area = ((Base-base) *altura)/2
            else:
                puntoMedio = (d-a)/2
                intervalo = d-a
                Base = d-a
                area = (Base*altura)-((altura**2)/2)


            self.numerador = self.numerador + (puntoMedio*area)
            self.denominador = self.denominador + area

        self.centroide = self.numerador/self.denominador

        for trap in self.trapecio:
            a,b,c,d,altura,etiqueta = trap
            if a <= self.centroide <=d:
                self.etiqueta = etiqueta
            else:
                pass

    def obtenerValorDesfusificado(self):
        return self.centroide

    def obtenerEtiquetaResultado(self):
        return self.etiqueta
#a,b,c,d,altura = (333, 530.4071856287426, 802.0, 1000, 0.592814371257485)

#puntoMedio = (d-a)/2
#intervalo = d-a
#base = c-b
#Base = d-a
#area = ((Base+base)*altura)/2
#centroide = 0
#print area
#centroide = centroide +((puntoMedio*(intervalo*area))/(intervalo*area))
#print centroide
