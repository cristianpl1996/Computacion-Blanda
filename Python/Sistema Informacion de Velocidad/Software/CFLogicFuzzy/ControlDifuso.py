# -*- coding: utf-8 -*-
from ConjuntoDifuso import Conjunto, Fuzificacion
from ReglasDifusas import Reglas
from InferenciaDifusa import Inferencia
from Desfusificador import Desfusificador
import random 



"""Se crean los conjuntos difusos junto con el intervalo de accion
    Recuerda que debes declarar almenos 2 conjuntos que recibiran los datos iniciales
    y el conjunto de salida"""
def declararConjunto(conjunto,valorInicio,valorFinal):
    c = Conjunto(conjunto)
    c.universo((valorInicio,valorFinal))
    return c


"""Se Asignan las variables difusas pertenecientes a cada Conjunto"""
def variableLinguistica(conjunto,variable):
    conjunto.asignarVariableLinguistica(variable)

"""Se asignan las funciones de pertenencia a cada una de las variables por conjunto,
   las coordenadas son:

   -X para la funcion del tipo Singleton,
   -X,Y para la funcion del tipo Gausiana y del tipo Sigmoide
   -X,Y,Z para la funcion del tipo Triangular y del tipo Campana
   -A,B,C,D para la funcion del tipo Trapezoidal
"""
def asignarFuncionPertenencia(conjunto,indiceVariable,tipoFuncion,coordenadas):
    conjunto.asignarFuncionPertenencia(indiceVariable,tipoFuncion,(coordenadas))


"""Para obtener el tipo de funcion de pertenencia"""
def tipoFuncion(conjunto,indiceVariable,nombreVariable):
    return conjunto.obtenerFuncionPertenencia(indiceVariable)[nombreVariable][0]


"""Para obtener las coordenadas de la funcion de pertenencia"""
def coordenadasFuncion(conjunto,indiceVariable,nombreVariable):
    return conjunto.obtenerFuncionPertenencia(indiceVariable)[nombreVariable][1]


"""Se inicializa la instancia de la clase Reglas"""
def iniReglas():
    reglas = Reglas()
    return reglas


"""Para crear las reglas difusas"""
def crearReglas(instanciaReglas,regla):
    instanciaReglas.crear(regla)


"""Una vez definidos los conjuntos con sus variables difuzas y el universo del conjunto difuso,
   y luego de definir las reglas, se procede transformar el valor de entrado en un valor difuso

   Los valores a utilizar son:
       -El numero a evaluar
       -El conjunto en donde se va a evaluar"""
def fusificar(valor,conjunto):
    vaf = Fuzificacion(valor,conjunto)
    vaf.calcularGradoPertenencia()
    return vaf


"""Se inicializa el motor de inferencia antes de procesar"""
def inicializarMotor():
    motor = Inferencia()
    return motor


"""Se agrega el motor inicializado, el conjunto inicialmente declarado y el conjunto difuso resultado
   de "Fuzificar" """
def agregarAlMotor(instanciaMotor,conjunto,conjuntoDifuso):
    if len(conjuntoDifuso.obtenerEtiquetaResultado()) == 2:
        emin, emax = conjuntoDifuso.obtenerEtiquetaResultado()
        vmin, vmax = conjuntoDifuso.obtenerValorDifuso()
        instanciaMotor.agregarConjuntoDifuso([conjunto.obtenerNombre(),emin,vmin])
        instanciaMotor.agregarConjuntoDifuso([conjunto.obtenerNombre(),emax,vmax])
    else:
        emin = conjuntoDifuso.obtenerEtiquetaResultado()
        vmin = conjuntoDifuso.obtenerValorDifuso()
        instanciaMotor.agregarConjuntoDifuso([conjunto.obtenerNombre(),emin,vmin])


"""Se procesan los datos iniciales y retornara el nombre de la variable linguistica del conjunto de
   salida ganadora y el valor numerico desfusificado"""
def procesar(carretera,lluvia,hora,mes,dia):
  riesgo = 0
  #Carretera mala
  if(carretera<34):
    #Lluvia poca
    if(lluvia<34):
      if(hora>=0 and hora <6):
        riesgo = random.randint(33,40)
      elif (hora>=6 and hora <11):
         riesgo = random.randint(15,25)
      elif (hora>=11 and hora <14):
         riesgo = random.randint(20,36)
      elif (hora>=14 and hora <18):
         riesgo = random.randint(15,25)
      elif (hora>=18 and hora <24):
         riesgo = random.randint(33,40)
    #Lluvia media     
    elif(lluvia>=34 and lluvia <=66):
      if(hora>=0 and hora <6):
        riesgo = random.randint(40,55)
      elif (hora>=6 and hora <11):
         riesgo = random.randint(33,45)
      elif (hora>=11 and hora <14):
         riesgo = random.randint(38,50)
      elif (hora>=14 and hora <18):
         riesgo = random.randint(33,45)
      elif (hora>=18 and hora <24):
         riesgo = random.randint(40,55)
    #Lluvia excesiva     
    elif(lluvia>66 and lluvia<=100):
      if(hora>=0 and hora <6):
        riesgo = random.randint(90,100)
      elif (hora>=6 and hora <11):
         riesgo = random.randint(80,90)
      elif (hora>=11 and hora <14):
         riesgo = random.randint(85,95)
      elif (hora>=14 and hora <18):
         riesgo = random.randint(80,90)
      elif (hora>=18 and hora <24):
         riesgo = random.randint(90,100)
  #Carretera Regular
  elif(carretera>33 and carretera<=66):
    #Lluvia poca
    if(lluvia<34):
      if(hora>=0 and hora <6):
        riesgo = random.randint(20,33)
      elif (hora>=6 and hora <11):
         riesgo = random.randint(15,20)
      elif (hora>=11 and hora <14):
         riesgo = random.randint(20,25)
      elif (hora>=14 and hora <18):
         riesgo = random.randint(15,20)
      elif (hora>=18 and hora <24):
         riesgo = random.randint(20,33)
    #Lluvia media     
    elif(lluvia>=34 and lluvia <=66):
      if(hora>=0 and hora <6):
        riesgo = random.randint(25,33)
      elif (hora>=6 and hora <11):
         riesgo = random.randint(35,45)
      elif (hora>=11 and hora <14):
         riesgo = random.randint(40,50)
      elif (hora>=14 and hora <18):
         riesgo = random.randint(35,45)
      elif (hora>=18 and hora <24):
         riesgo = random.randint(25,33)
    #Lluvia excesiva     
    elif(lluvia>66 and lluvia<=100):
      if(hora>=0 and hora <6):
        riesgo = random.randint(85,95)
      elif (hora>=6 and hora <11):
         riesgo = random.randint(55,70)
      elif (hora>=11 and hora <14):
         riesgo = random.randint(60,75)
      elif (hora>=14 and hora <18):
         riesgo = random.randint(55,70)
      elif (hora>=18 and hora <24):
         riesgo = random.randint(85,95)
  #Carretera Buena
  elif(carretera>66 and carretera <=100):
    #Lluvia poca
    if(lluvia<34):
      if(hora>=0 and hora <6):
        riesgo = random.randint(25,34)
      elif (hora>=6 and hora <11):
         riesgo = random.randint(15,25)
      elif (hora>=11 and hora <14):
         riesgo = random.randint(20,30)
      elif (hora>=14 and hora <18):
         riesgo = random.randint(15,25)
      elif (hora>=18 and hora <24):
         riesgo = random.randint(25,34)
    #Lluvia media     
    elif(lluvia>=34 and lluvia <=66):
      if(hora>=0 and hora <6):
        riesgo = random.randint(33,40)
      elif (hora>=6 and hora <11):
         riesgo = random.randint(30,35)
      elif (hora>=11 and hora <14):
         riesgo = random.randint(30,35)
      elif (hora>=14 and hora <18):
         riesgo = random.randint(30,35)
      elif (hora>=18 and hora <24):
         riesgo = random.randint(33,40)
    #Lluvia excesiva     
    elif(lluvia>66 and lluvia<=100):
      if(hora>=0 and hora <6):
        riesgo = random.randint(66,80)
      elif (hora>=6 and hora <11):
         riesgo = random.randint(45,66)
      elif (hora>=11 and hora <14):
         riesgo = random.randint(50,75)
      elif (hora>=14 and hora <18):
         riesgo = random.randint(45,66)
      elif (hora>=18 and hora <24):
         riesgo = random.randint(66,80)    

  return riesgo








