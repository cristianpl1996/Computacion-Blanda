# -*- coding: utf-8 *-*
"""
    Crea las reglas difusas siguiendo el siguiente formato:

    "if Conjunto is VariableLinguistica and Conjunto is VariableLinguistica then Conjunto is VariableLinguistica"


    Este formato debe ser respetado para que pueda ser procesado y desfuzificado.

    -El "Conjunto" es el nombre de la variable creada.
    -La "VariableLinguistica" es la etiqueta perteneciente al conjunto creado.
"""

class Reglas:

    def __init__(self):
        self.regla = ""
        self.reglas = []


    def crear(self,regla):
        self.regla = regla
        self.reglas.append(self.regla)

    def obtenerReglas(self):
        return self.reglas

