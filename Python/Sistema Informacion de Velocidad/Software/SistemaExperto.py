from pyDatalog import pyDatalog

pyDatalog.create_terms('Velocidad, V, Accidentalidad, Velocidad_Sugerida')

#Base del Conocimiento
+Velocidad(0,"70-90")
+Velocidad(1,"50-60") 
+Velocidad(2,"30-40") 
+Velocidad(3,"10-30") 
#Reglas
V(Accidentalidad,Velocidad_Sugerida) <= Velocidad(Accidentalidad,Velocidad_Sugerida)
