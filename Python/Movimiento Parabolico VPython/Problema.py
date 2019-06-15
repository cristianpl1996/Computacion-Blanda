import Solucion

def problema(area,componente,modulo):
	if (area==Solucion.area) and (componente==Solucion.componente) and (modulo==Solucion.modulo):
		Respuesta=Solucion.f(50,15)
		print "La Distancia total Recorrida en X es:",Respuesta
	else:
		print "No tenemos Solucion para el problema"

area="fisica"
componente="cinematica"
modulo="movimiento_parabolico"
problema(area,componente,modulo)			