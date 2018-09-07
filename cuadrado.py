import math
import sys

def isCuadrado(*args):
    #si no son cuatro tuplas, no es un cuadrado
    if len(args)!=4:
        return false
    #array de distancias
    distancias = []
    #recorre los argumentos y calcula distancias con cada uno de los otros 3 puntos
    for i in range(len(args)):
        options = [0,1,2,3]
        options.remove(i)
        for j in options:
            dist = distancia(args[i], args[j])
            #no lo agrega si ya existe, en un cuadrado solo existen dos distancias unicas
            if dist not in distancias:
                distancias.append(dist)
    #si en el arreglo hay mas de dos distancias, no es un cuadrado
    return len(distancias) == 2

def distancia(p1, p2):
    xd = pow((p1[0] - p2[0]), 2)
    yd = pow((p1[1] - p2[1]), 2)
    dist = math.sqrt(xd + yd)
    return dist

    

