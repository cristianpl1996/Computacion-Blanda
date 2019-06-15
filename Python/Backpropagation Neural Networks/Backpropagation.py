# Backpropagation Neural Networks
import math, random

# Derivada de la funcion de activacion
def DerivadaFA(y):
    return 1.0 - y**2

# Funcion de activacion, se descoge la Tangente Hiperbolica porque es mejor que la Sigmoid, 1/(1+e^-x)
def FuncionActivacion(x):
    return math.tanh(x)

# Crear Matriz 
def CrearMatriz(i, j):
    m = []
    for x in range(i):
        m.append([0.0]*j)
    return m
#Implementacion de la clase RedNeuronal
class RedNeuronal:
    def __init__(self, ni, nh, no):
        # Numero de nodos de capa entradas, capa oculta, capa de salida 
        self.ni = ni + 1 # +1 para el bias
        self.nh = nh
        self.no = no

        #Variables
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no

        # Crear matriz de pesos y asignar valores aleatorios
        self.wi = CrearMatriz(self.ni, self.nh)
        self.wo = CrearMatriz(self.nh, self.no)

        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = random.uniform(-0.1,0.1)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = random.uniform(-0.1,0.1)
   
    def update(self, inputs):
        # Asigna las  entradas a la variable ai
        for i in range(self.ni-1):
            self.ai[i] = inputs[i]

        # Sumatoria de entradas * pesos, Activacion de la capa oculta 
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = FuncionActivacion(sum)

        # Sumatoria de entradas * pesos, Activacion de la capa salida
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = FuncionActivacion(sum)

        return self.ao

    def Backpropagation(self, outputs, N):
        # calcular errores en la capa de salida
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = outputs[k]-self.ao[k]
            output_deltas[k] = DerivadaFA(self.ao[k]) * error

        # calcular errores en la capa oculta
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = DerivadaFA(self.ah[j]) * error

        # Actualizar los pesos de la capa de salida
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change

       # Actualizar los pesos de la capa de entrada
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change

        return error

    def Resultado(self, patron):
        for p in patron:
            salida=self.update(p[0])
            aux1,aux2=[],[]
            for x in salida:
                aux1.append(format(x,".5f"))
                aux2.append(int(round(x)))
            print p[0], "->",aux1,"->",aux2

    def Entrenamiento(self, patron, iteraciones=1000, N=0.16):
        # N: Tasa de Aprendizaje
        for i in range(iteraciones):
            error = 0.0
            for p in patron:
                inputs = p[0]
                outputs = p[1]
                self.update(inputs)
                error = error + self.Backpropagation(outputs, N)
            if i % 200 == 0:
                print 'error: %-.5f' % error

def main():
    """ # Datos de entrenamiento para una compuerta logica XOR
    XOR = [
        [[0,0], [0]],
        [[0,1], [1]],
        [[1,0], [1]],
        [[1,1], [0]]]
    # Crea una Red Neuronal con 2 nodos entradas, 2 nodos ocultos, 1 nodo de salida
    r1 = RedNeuronal(2,2,1)
    # Entrenamiento de la XOR
    r1.Entrenamiento(XOR)
    # Resultado de la Red Neuronal
    r1.Resultado(XOR)"""

    Leds=[
        [[1,1,1,1,1,1,0],[0,0,0,0]],
        [[0,1,1,0,0,0,0],[0,0,0,1]],
        [[1,1,0,1,1,0,1],[0,0,1,0]],
        [[1,1,1,1,0,0,1],[0,0,1,1]],
        [[0,1,1,0,0,1,1],[0,1,0,0]],
        [[1,0,1,1,0,1,1],[0,1,0,1]],
        [[1,0,1,1,1,1,1],[0,1,1,0]],
        [[1,1,1,0,0,0,1],[0,1,1,1]],
        [[1,1,1,1,1,1,1],[1,0,0,0]],
        [[1,1,1,1,0,1,1],[1,0,0,1]]]

    r2 = RedNeuronal(7,5,4)
    r2.Entrenamiento(Leds)
    r2.Resultado(Leds)

if __name__ == '__main__':
    main()