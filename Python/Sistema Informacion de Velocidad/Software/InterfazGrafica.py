#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from ttk import *
import tkMessageBox
from LogicaDifusa import *
from Backpropagation import *
from SistemaExperto import *
from geopy.geocoders import Nominatim

#Variables Globales
estado_Carretera=0
presencia_Lluvia=0
hora=0
dia=0
mes=0
bandera1=False
bandera2=False
bandera3=False
bandera4=False
bandera5=False
bandera6=False
bandera7=False
riesgo=0
accidentalidad=0
x,y=0,0

def Ubicacion(coordenadas):
	geolocator = Nominatim(user_agent="Sistema de Información de Velocidad")
	location = geolocator.reverse(coordenadas)
	print location.address
	ubicacion=[]
	cadena=""
	i=0
	for x in location.address:
		i=i+1
		if x == "," or i == len(location.address):
			ubicacion.append(cadena)
			cadena=""	
		else:
			cadena=cadena+x	
	return ubicacion

def main():
	#Interfaz Grafica	
	window = Tk()
	window.geometry('350x200')
	window.title("Sistema Control de Velocidad ©")
	window.resizable(0,0) 
	bit = window.iconbitmap('images/icono.ico')
	fondo=PhotoImage(file="images/fondo.gif")
	lblImageFondo=Label(window,image=fondo).place(x=0,y=0)
	lbl1 = Label(window, text="Estado de Carretera")
	lbl1.grid(column=0, row=0)
	txt1 = Entry(window,width=15)
	txt1.insert(0,0)
	txt1.grid(column=1, row=0)
	lbl2 = Label(window, text="Presencia de LLuvia")
	lbl2.grid(column=0, row=2)
	txt2 = Entry(window,width=15)
	txt2.insert(0,0)
	txt2.grid(column=1, row=2)
	lbl3 = Label(window, text="Hora Militar")
	lbl3.grid(column=0, row=1)
	txt3 = Entry(window,width=15)
	txt3.insert(0,0)
	txt3.grid(column=1, row=1)
	lbl4 = Label(window, text="Dia")
	lbl4.grid(column=0, row=3)
	combo1 = Combobox(window,width=12)
	combo1['values'] = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo") 
	combo1.current(0)
	combo1.grid(column=1, row=3)
	lbl5 = Label(window, text="Mes")
	lbl5.grid(column=0, row=4)
	combo2 = Combobox(window,width=12)
	combo2['values'] = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre") 
	combo2.current(0)
	combo2.grid(column=1, row=4)
	lbl6 = Label(window, text="Riesgo")
	lbl6.grid(column=4, row=0)
	txt4 = Entry(window,width=15,state='disabled')
	txt4.grid(column=5, row=0)
	lbl7 = Label(window, text="Latitud")
	lbl7.grid(column=4, row=1)
	txt5 = Entry(window,width=15,state='disabled')
	txt5.grid(column=5, row=1)
	lbl8 = Label(window, text="Longitud")
	lbl8.grid(column=4, row=2)
	txt6 = Entry(window,width=15,state='disabled')
	txt6.grid(column=5, row=2)
	lbl9 = Label(window, text="Velocidad")
	lbl9.grid(column=4, row=5)
	txt7 = Entry(window,width=15,state='disabled')
	txt7.grid(column=5, row=5)
	lbl10 = Label(window, text="Ubicacion")
	lbl10.grid(column=4, row=4)
	txt8 = Entry(window,width=15,state='disabled')
	txt8.grid(column=5, row=4)
	# Evento 1 boton
	def clicked1():
		global estado_Carretera, presencia_Lluvia,hora,dia,mes,bandera1,bandera2,bandera3,bandera4,bandera5,riesgo
		try:
			if int(txt1.get())>=0 and int(txt1.get())<=100: 
				estado_Carretera=int(txt1.get())
				bandera1=True
			else:
				bandera1=False

			if int(txt2.get())>=0 and int(txt2.get())<=100: 
				presencia_Lluvia=int(txt2.get())
				bandera2=True
			else:
				bandera2=False

			if int(txt3.get())>=0 and int(txt3.get())<=23: 
				hora=int(txt3.get())
				bandera3=True
			else:
				bandera3=False				
		except ValueError:
			tkMessageBox.showerror('Error', 'TIPO DE DATO ERRONEO')

		if combo1.get()=="Lunes":
			dia=1
			bandera4=True
		elif combo1.get()=="Martes":
			dia=2
			bandera4=True
		elif combo1.get()=="Miercoles":
			dia=3
			bandera4=True
		elif combo1.get()=="Jueves":
			dia=4
			bandera4=True
		elif combo1.get()=="Viernes":
			dia=5
			bandera4=True
		elif combo1.get()=="Sabado":
			dia=6
			bandera4=True
		elif combo1.get()=="Domingo":
			dia=7
			bandera4=True
		else:
			bandera4=False

		if combo2.get()=="Enero":
			mes=1
			bandera5=True
		elif combo2.get()=="Febrero":
			mes=2
			bandera5=True
		elif combo2.get()=="Marzo":
			mes=3
			bandera5=True
		elif combo2.get()=="Abril":
			mes=4
			bandera5=True
		elif combo2.get()=="Mayo":
			mes=5
			bandera5=True
		elif combo2.get()=="Junio":
			mes=6
			bandera5=True
		elif combo2.get()=="Julio":
			mes=7
			bandera5=True
		elif combo2.get()=="Agosto":
			mes=8
			bandera5=True
		elif combo2.get()=="Septiembre":
			mes=9
			bandera5=True
		elif combo2.get()=="Octubre":
			mes=10
			bandera5=True
		elif combo2.get()=="Noviembre":
			mes=11
			bandera5=True
		elif combo2.get()=="Diciembre":
			mes=12
			bandera5=True					
		else:
			bandera5=False	
			
		if bandera1 and bandera2 and bandera3 and bandera4 and bandera5:	
			txt1.configure(state='disabled')
			txt2.configure(state='disabled')
			txt3.configure(state='disabled')
			combo1.configure(state='disabled')
			combo2.configure(state='disabled')
			btn1.configure(state='disabled')
			txt4.configure(state="enable")
			#Logica Difusa
			riesgo = CalcularRiesgo(estado_Carretera,presencia_Lluvia,hora,dia,mes)
			txt4.insert(0,riesgo)
			txt4.configure(state="disable")
			txt5.configure(state='enable')
			txt6.configure(state='enable')
			btn2.configure(state='enable')
			txt7.configure(state="enable")
			txt7.delete(0,10)
			txt7.configure(state="disable")
			txt8.configure(state="enable")
			txt8.delete(0,30)
			txt8.configure(state="disable")
	# Evento 2 boton		
	def clicked2():
		global x, y, bandera6, bandera7, riesgo, accidentalidad
		try:
			if float(txt5.get())>=-90 and float(txt5.get())<=90: 
				x=txt5.get()
				bandera6=True
			else:
				bandera6=False

			if float(txt6.get())>=-180 and float(txt6.get())<=180: 
				y=txt6.get()
				bandera7=True
			else:
				bandera7=False
				
		except ValueError:
			tkMessageBox.showerror('Error', 'TIPO DE DATO ERRONEO')

		if bandera6 and bandera7:	
			txt1.configure(state='enable')
			txt1.delete(0,10)
			txt1.insert(0,0)
			txt2.configure(state='enable')
			txt2.delete(0,10)
			txt2.insert(0,0)
			txt3.configure(state='enable')
			txt3.delete(0,10)
			txt3.insert(0,0)
			combo1.configure(state='enable')
			combo1.current(0)
			combo2.configure(state='enable')
			combo2.current(0)
			btn1.configure(state='enable')
			txt4.configure(state="enable")
			txt4.delete(0,10)
			txt4.configure(state="disable")
			txt5.delete(0,15)
			txt5.configure(state='disable')
			txt6.delete(0,15)
			txt6.configure(state='disable')
			btn2.configure(state='disabled')
			#Geopy - Ubicacion de Principales Vias
			coordenadas=x+","+y
			ubicacion=Ubicacion(coordenadas)[0]
			d=[]
			if ubicacion == "Avenida de las Americas":
				d=[0,0,0,0]
			elif ubicacion == "Maraya":
				d=[0,0,0,1]
			elif ubicacion == "Calle 70":
				d=[0,0,1,0]
			elif ubicacion == "Centenario":
				d=[0,0,1,1]
			elif ubicacion == "Avenida Circunvalar":
				d=[0,1,0,0]
			elif ubicacion == "Avenida del Río":
				d=[0,1,0,1]
			elif ubicacion == "Calle 13":
				d=[0,1,1,0]	
			elif ubicacion == "Carrera 16":
				d=[0,1,1,1]	
			elif ubicacion == "Confamiliar":
				d=[1,0,0,0]	
			elif ubicacion == "Carrera 8":
				d=[1,0,0,1]	
			elif ubicacion == "Carrera 4":
				d=[1,0,1,0]
			elif ubicacion == "Calle 7":
				d=[1,0,1,1]
			elif ubicacion == "Carrera 12":
				d=[1,1,0,0]
			elif ubicacion == "San Jose Sur":
				d=[1,1,0,1]	
			elif ubicacion == "Colegio Cooperativo":
				d=[1,1,1,0]	
			elif ubicacion == "Calle 12":
				d=[1,1,1,1]
			else:
				d=[0,0,0,0]																	
			#Red Neuronal Backpropagation
			e=Binario(riesgo)
			entrada=[[[e[0],e[1],e[2],e[3],e[4],e[5],e[6],d[0],d[1],d[2],d[3]],[0,0]]]
			accidentalidad=0
			output =red.Resultado(entrada)
			if output[0]==0 and output[1]==0:
			    accidentalidad=0
			elif output[0]==0 and output[1]==1:
			    accidentalidad=1
			elif output[0]==1 and output[1]==0:
			    accidentalidad=2
			elif output[0]==1 and output[1]==1:
			    accidentalidad=3 
			#Sistema Experto    
			V(accidentalidad,Velocidad_Sugerida)
			print "Velocidad Sugerida:",Velocidad_Sugerida.v(),"km/h"
			txt7.configure(state="enable")
			velocidad=Velocidad_Sugerida.v()
			txt7.insert(0,velocidad+" km/h")
			txt7.configure(state="disable")
			txt8.configure(state="enable")
			txt8.insert(0,ubicacion)
			txt8.configure(state="disable")

	btn1 = Button(window, width=14, text="Enviar", command=clicked1)
	btn1.grid(column=1, row=5)
	btn2 = Button(window, width=14, text="Enviar", command=clicked2, state="disable")
	btn2.grid(column=5, row=3)
	window.mainloop()

if __name__ == '__main__':
	main()