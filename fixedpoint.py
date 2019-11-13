
#Imports
import math
import numpy as np
from matplotlib import pyplot as plt

#input

x = 1
tol = 0.0001

def f(x):                           #Funcion f(x)

    efe = x*math.e**(0.5*x)+1.2*x-5

    return efe


def funciong(x):                    # g(x) funcion de iteración

    fun = ((5)/(math.e**(0.5*x)+1.2))

    return fun


def funDer(x):                      # f'(x), f(x) derivada

    der = ((-5*math.e**(0.5*x))/(2*(math.e**(0.5*x)+1.2)**(2)))

    return der

def fgraph(x):                      #función para graficar

    return x

def zero(x):                        #función para graficar

    return 0


def fixed(f,g,fprim,x1, tol):       #Función de punto fijo
    it = 0

    if(np.abs(fprim(x1)) < 1):      #|f'(x)|<1 (Converge o Diverge)

        while(np.abs(f(x1)) > tol): #Condición de iteración (|f(x1)|> tolerancia)
            x_n = g(x1)             #x_n -> x nueva 
            x1 = x_n
            it += 1
            
        return print('\nResultado:\n' , x_n,'\nIteraciones:\n', it, '\n')
    else:
        print('Diverge.', '\n')

fixed(f,funciong,funDer,x, tol)      #Llamada a la función con los paramentros

#Gráfica
a1 = 1
b1 = 3
paso = 0.1
x = np.arange(a1, b1, paso)
x1 = np.arange(a1, b1, paso)


Y_F = [f(i) for i in x1]
Y_G = [funciong(i) for i in x]
Y_F1 = [fgraph(i) for i in x]
Y_0 = [zero(i) for i in x]

fig1 = plt.figure()
axe = fig1.add_subplot(1, 1, 1)
axe.plot(x1, Y_F, 'b', label='f(x)')
axe.plot(x, Y_G, 'y', label='g(x)',  linestyle='--')
axe.plot(x, Y_F1, 'r', label='x',  linestyle='--')
axe.plot(x, Y_0, 'g')

axe.legend()
plt.ylabel("y")
plt.xlabel("x")
plt.title("Punto Fijo")
plt.show()
