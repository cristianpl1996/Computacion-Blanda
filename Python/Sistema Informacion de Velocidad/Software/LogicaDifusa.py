# -*- coding: utf-8 -*-
from CFLogicFuzzy import ControlDifuso as ld

#Variables: Estado_carretera, Presencia_lluvia, Hora, Dia, Mes, Riesgo

Estado_carretera = ld.declararConjunto("Estado_carretera",0,100)
ld.variableLinguistica(Estado_carretera,"Mala")
ld.variableLinguistica(Estado_carretera,"Regular")
ld.variableLinguistica(Estado_carretera,"Buena")

ld.asignarFuncionPertenencia(Estado_carretera,0,"Triangular",(0,33,66))
ld.asignarFuncionPertenencia(Estado_carretera,1,"Triangular",(33,66,100))
ld.asignarFuncionPertenencia(Estado_carretera,2,"Trapezoidal_Derecho",(66,100))


Presencia_lluvia = ld.declararConjunto("Presencia_lluvia",0,100)
ld.variableLinguistica(Presencia_lluvia,"Poca")
ld.variableLinguistica(Presencia_lluvia,"Moderada")
ld.variableLinguistica(Presencia_lluvia,"Excesiva")

ld.asignarFuncionPertenencia(Presencia_lluvia,0,"Triangular",(0,33,66))
ld.asignarFuncionPertenencia(Presencia_lluvia,1,"Triangular",(33,66,100))
ld.asignarFuncionPertenencia(Presencia_lluvia,2,"Trapezoidal_Derecho",(66,100))


Hora = ld.declararConjunto("Hora",0,23)
ld.variableLinguistica(Hora,"Madrugada")
ld.variableLinguistica(Hora,"Mañana")
ld.variableLinguistica(Hora,"Medio_dia")
ld.variableLinguistica(Hora,"Tarde")
ld.variableLinguistica(Hora,"Noche")

ld.asignarFuncionPertenencia(Hora,0,"Triangular",(0,6,9))
ld.asignarFuncionPertenencia(Hora,1,"Triangular",(6,9,11))
ld.asignarFuncionPertenencia(Hora,2,"Triangular",(11,13,14))
ld.asignarFuncionPertenencia(Hora,3,"Triangular",(14,16,18))
ld.asignarFuncionPertenencia(Hora,4,"Triangular",(18,21,23))

Dia = ld.declararConjunto("Dia",1,7)
ld.variableLinguistica(Dia,"Lunes")
ld.variableLinguistica(Dia,"Martes")
ld.variableLinguistica(Dia,"Miercoles")
ld.variableLinguistica(Dia,"Jueves")
ld.variableLinguistica(Dia,"Viernes")
ld.variableLinguistica(Dia,"Sabado")
ld.variableLinguistica(Dia,"Domingo")

ld.asignarFuncionPertenencia(Dia,0,"Singleton",(1,1))
ld.asignarFuncionPertenencia(Dia,1,"Singleton",(2,2))
ld.asignarFuncionPertenencia(Dia,2,"Singleton",(3,3))
ld.asignarFuncionPertenencia(Dia,3,"Singleton",(4,4))
ld.asignarFuncionPertenencia(Dia,4,"Singleton",(5,5))
ld.asignarFuncionPertenencia(Dia,5,"Singleton",(6,6))
ld.asignarFuncionPertenencia(Dia,6,"Singleton",(7,7))

Mes = ld.declararConjunto("Mes",1,12)
ld.variableLinguistica(Mes,"Enero")
ld.variableLinguistica(Mes,"Febrero")
ld.variableLinguistica(Mes,"Marzo")
ld.variableLinguistica(Mes,"Abril")
ld.variableLinguistica(Mes,"Mayo")
ld.variableLinguistica(Mes,"Junio")
ld.variableLinguistica(Mes,"Julio")
ld.variableLinguistica(Mes,"Agosto")
ld.variableLinguistica(Mes,"Septiembre")
ld.variableLinguistica(Mes,"Octubre")
ld.variableLinguistica(Mes,"Noviembre")
ld.variableLinguistica(Mes,"Diciembre")

ld.asignarFuncionPertenencia(Mes,0,"Singleton",(1,1))
ld.asignarFuncionPertenencia(Mes,1,"Singleton",(2,2))
ld.asignarFuncionPertenencia(Mes,2,"Singleton",(3,3))
ld.asignarFuncionPertenencia(Mes,3,"Singleton",(4,4))
ld.asignarFuncionPertenencia(Mes,4,"Singleton",(5,5))
ld.asignarFuncionPertenencia(Mes,5,"Singleton",(6,6))
ld.asignarFuncionPertenencia(Mes,6,"Singleton",(7,7))
ld.asignarFuncionPertenencia(Mes,7,"Singleton",(8,8))
ld.asignarFuncionPertenencia(Mes,8,"Singleton",(9,9))
ld.asignarFuncionPertenencia(Mes,9,"Singleton",(10,10))
ld.asignarFuncionPertenencia(Mes,10,"Singleton",(11,11))
ld.asignarFuncionPertenencia(Mes,11,"Singleton",(12,12))

Riesgo = ld.declararConjunto("Riesgo",0,100)
ld.variableLinguistica(Riesgo,"Bajo")
ld.variableLinguistica(Riesgo,"Medio")
ld.variableLinguistica(Riesgo,"Alto")

ld.asignarFuncionPertenencia(Riesgo,0,"Triangular",(0,33,66))
ld.asignarFuncionPertenencia(Riesgo,1,"Triangular",(33,66,100))
ld.asignarFuncionPertenencia(Riesgo,2,"Trapezoidal_Derecho",(66,100))

reglas = ld.iniReglas()
ld.crearReglas(reglas,"if Estado_carretera is Mala and Presencia_lluvia is Poca then Riesgo Medio")
ld.crearReglas(reglas,"if Estado_carretera is Mala and Presencia_lluvia is Moderada then Riesgo Alto")
ld.crearReglas(reglas,"if Estado_carretera is Mala and Presencia_lluvia is Excesiva then Riesgo Alto")
ld.crearReglas(reglas,"if Estado_carretera is Regular and Presencia_lluvia is Poca then Riesgo Bajo")
ld.crearReglas(reglas,"if Estado_carretera is Regular and Presencia_lluvia is Moderada then Riesgo Medio")
ld.crearReglas(reglas,"if Estado_carretera is Regular and Presencia_lluvia is Excesiva then Riesgo Medio")
ld.crearReglas(reglas,"if Estado_carretera is Buena and Presencia_lluvia is Poca then Riesgo Bajo")
ld.crearReglas(reglas,"if Estado_carretera is Buena and Presencia_lluvia is Moderada then Riesgo Medio")
ld.crearReglas(reglas,"if Estado_carretera is Buena and Presencia_lluvia is Excesiva then Riesgo Medio")

def CalcularRiesgo(A,B,C,D,E):
	festadocarretera = ld.fusificar(A,Estado_carretera)
	fpresencialluvia = ld.fusificar(B,Presencia_lluvia)
	fhora = ld.fusificar(C,Hora)
	fdia = ld.fusificar(D,Dia)
	fmes = ld.fusificar(E,Mes)
	motor = ld.inicializarMotor()
	ld.agregarAlMotor(motor,Estado_carretera,festadocarretera)
	ld.agregarAlMotor(motor,Presencia_lluvia,fpresencialluvia)
	ld.agregarAlMotor(motor,Hora,fhora)
	ld.agregarAlMotor(motor,Dia,fdia)
	ld.agregarAlMotor(motor,Mes,fmes)
	Resultado = ld.procesar(A,B,C,D,E)
	return Resultado










