# -*- coding: utf-8 *-*
"""
    La clase inferencia procesa las el conjunto difuso junto con las reglas
    establecidas, para al final devolver los trapecios que seran desfusificados
"""

class Inferencia:

    def __init__(self):
        self.reglas = []
        self.conjunto = []
        self.condiciones = []
        self.actuaciones = []
        self.listaReglas = []
        self.parCon = []
        self.trapecio = []

    def procesarReglas(self):

        entonces = False

        for regla in self.reglas:
            rlimp = regla.split(' ')
            for word in rlimp:

                if word == "then":
                    entonces = True


                if not entonces:
                    if word == "if":
                        pass
                    else:
                        self.condiciones.append(word)
                else:
                    if word == "then":
                        pass
                    else:
                        self.actuaciones.append(word)
            while "is" in self.condiciones:
                self.condiciones.remove("is")
            while "is" in self.actuaciones:
                self.actuaciones.remove("is")
            self.listaReglas.append([self.condiciones,self.actuaciones])
            self.condiciones = []
            self.actuaciones = []
            entonces = False

    def agregarConjuntoDifuso(self,fuzzyset):
        self.conjunto.append(fuzzyset)

    def agregarReglas(self,regla):
        self.reglas.append(regla)

    def obtenerCondiciones(self):
        return self.condiciones

    def obtenerActuaciones(self):
        return self.actuaciones

    def motorDifuso(self,Conjunto):
        self.conjuntoSalida = Conjunto
        auxa = False
        auxo = False
        auxn = False
        v1 = ""
        v2 = ""
        v3 = ""
        v4 = ""
        cond = []
        actu = []


        for lr in self.listaReglas:

            for i, parte in enumerate(lr):
                if i == 0:
                    for palabra in parte:
                        if palabra == "and":
                            auxa = True
                        if auxa:
                            if palabra == "and":
                                v1 = ""
                                v2 = ""
                                pass
                        else:
                            if v1=="":
                                v1 = palabra
                            else:
                                v2 = palabra
                            for c in self.conjunto:
                                if v1 in c:
                                    if v2 in c:
                                        cond.append((v1,v2,c[2]))
                                        v1 = ""
                                        v2 = ""
                        auxa = False
                else:
                    for palabra in parte:
                        if palabra == "and":
                            auxa = True
                        if auxa:
                            if palabra == "and":
                                v3 = ""
                                v4 = ""
                                pass
                        else:
                            if v3=="":
                                v3 = palabra
                            else:
                                v4 = palabra
                    actu.append((v3,v4))
                    v3 = ""
                    v4 = ""
                    auxa = False
            self.parCon.append([cond,actu])
            cond = []
            actu = []

        self.truncarSalida(self.conjuntoSalida)
        print self.trapecio
        return self.trapecio

    def truncarSalida(self,Conjunto):
        self.cs = Conjunto

        for resultado in self.parCon:
            if resultado[0] == []:
                pass
            else:
                if len(resultado[0]) > 1:
                    """Comparamos las condiciones declaradas en las reglas con sus grados
                       de pertenencia para procesar el valor minimo y el valor maximo para
                       luego truncar los triangulos  de los valores obtenidos"""

                    x,y = resultado[0]

                    conjuntox, varlingx, alturax = x
                    conjuntoy, varlingy, alturay = y
                    valmin = min(alturax,alturay)

                    if valmin in x:
                        conjunto, varling, altura = x
                    if valmin in y:
                        conjunto, varling, altura = y

                    conjsalida, valSalida = resultado[1][0]
                    print conjsalida, valSalida

                    """Comparamos las instancias de ConjuntoDifuso para poder determinar con
                       cuales variables linguisticas y de cual instancia se va a trabajar"""
                    for ins in self.cs.__class__.instances:
                        if ins.nombre == conjsalida:
                            for i, insvl in enumerate(ins.vl):
                                if insvl.keys()[0] == valSalida:
                                    if len(insvl[valSalida][1]) == 2:
                                        for fpi in self.cs.__class__.instances:
                                            if fpi.nombre == conjunto:
                                                print fpi.obtenerFuncionPertenenciaPorValor(varling)
                                                if fpi.obtenerFuncionPertenenciaPorValor(varling) == "Trapezoidal_Derecho":
                                                    #Obtenemos las coordenadas de la funcion de pertenencia del valor instanciado
                                                    a,b = insvl[valSalida][1]
                                                    #Calculamos la x en donde sera la altura maxima del lado derecho
                                                    x = altura * (b-a) + a
                                                    #Por ultimo, Guardamos las coordenadas del trapecio creado
                                                    self.trapecio.append((a,x,b,b,altura,insvl.keys()[0]))

                                                if fpi.obtenerFuncionPertenenciaPorValor(varling) == "Trapezoidal_Izquierdo":
                                                    #Obtenemos las coordenadas de la funcion de pertenencia del valor instanciado
                                                    a,b = insvl[valSalida][1]
                                                    #Calculamos la x en donde sera la altura maxima del lado derecho
                                                    x = b - altura * (b-a)
                                                    #Por ultimo, Guardamos las coordenadas del trapecio creado
                                                    self.trapecio.append((a,a,x,b,altura,insvl.keys()[0]))

                                    else:

                                        #Obtenemos las coordenadas de la funcion de pertenencia del valor instanciado
                                        a,b,c = insvl[valSalida][1]

                                        """Ahora truncamos el triangulo en un trapecio con el valor minimo que
                                           #desfusificaremos, la altura del trapecio sera la obtenida por cada
                                           #regla aplicada al conjunto difuso"""

                                        #Calculamos la x en donde sera la altura maxima del lado izquierdo
                                        x = altura * (b-a) + a

                                        #Calculamos la x en donde sera la altura maxima del lado derecho
                                        x1 = c - altura * (c-b)

                                        #Por ultimo, Guardamos las coordenadas del trapecio creado
                                        self.trapecio.append((a,x,x1,c,altura,insvl.keys()[0]))
