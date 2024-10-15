import random
from biblia_funciones import *

matriz_cuadrada = inicializar_matriz(3, 3, 0)

imprimir_matriz(matriz_cuadrada)

cargar_matriz_secuencialmente(matriz_cuadrada)

imprimir_matriz(matriz_cuadrada)

matriz_sumada = sumatoria_fila(matriz_cuadrada)

print(matriz_sumada)



'''
    [8, 1, 6]               
    [3, 5, 7]               
    [4, 9, 2]               

    son_todas_iguales([15,15,15])

    M = n(n2 + 1)/2

        un cuadrado mágico de orden n, es
una matriz cuadrada de nxn donde los números
enteros del 1 al n2

1 al n2
1 al 44
1 al 16

DATO IMPORTANTE: no es válido para matrices de 2x2
'''
