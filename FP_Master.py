#Libreriasa necesarias
from scipy import optimize
import numpy as np
import decimal
from scipy._lib._util import _asarray_validated, _lazywhere


def sp_helper(actual, desired):
    return (actual - desired) / desired                 #Funcion auxiliar para calcular diferencial

def fixedPoint(function, x0, args, tol, maxit):
    p0 = x0 
    for i in range(maxit):                              #Iterar hasta le maximo de iteraciones

        p1 = function(p0, *args)                        #Vector resultante

        p=p1                                            #Variable temporal

        relerr = _lazywhere(p0 != 0, (p, p0), f=sp_helper, fillvalue=p)     #Funcion aux.
        if(np.all(np.abs(relerr) < tol)):               #Condición de iteración
            return p

        p0 = p

    msg = "Failed to converge after %d iterations, value is %s" % (maxit, p)
    raise RuntimeError(msg)


def auxFixedPoint(function, x0, maxit, tol, args=()):

    x0 = _asarray_validated(x0, as_inexact=True)    #Verifica si los vectores ingresados son validos 

    return fixedPoint(function, x0, args, tol, maxit)

def function(x,c1,c2):                          #Vector coumna con n funciones
    
    z = np.sqrt(c1/(x+c2))

    return z


c1 = np.array([1, 12])                  #Vector columna
c2 = np.array([1, 5])                   #Vector columna 
x0 = np.array([10, 20])                 #Vector inicial 


mit = input("Ingrese el maximo de iteraciones deseado: \n")
tole = input("Ingrese el nivel de tolerancia deseado (Recomendadp: 1e-8): \n")

maxit = int(mit)
tol = decimal.Decimal(tole)


print("Resultado: \n", auxFixedPoint(function, x0, maxit, tol, args=(c1, c2)), "\n")

