import random
import numpy as np
import time
import matplotlib.pylab as plt
#import threading

matriz = []

tam = 20
ejecuciones = 100




for i2 in range(0,tam):
    lin = []
    for i in range (0,tam):
        val = random.randint(0,1)
        lin.append(val)
    matriz.append(lin)



# matriz[fila][columna]
#print(np.asarray(matriz))

def vivir(fila, columna, vivo):
    cnt = 0
    for i in range(columna - 1, columna + 2):
        valor = encontrar(fila - 1, i)
        if valor != None:
            cnt += valor
    
    for i in range(columna - 1, columna + 2):
        valor = encontrar(fila, i)
        if valor != None and i != columna:
            cnt += valor

    for i in range(columna - 1, columna + 2):
        valor = encontrar(fila + 1, i)
        if valor != None:
            cnt += valor

    if vivo == 0:
        if cnt == 3:
            return 1
        else:
            return 0
    elif vivo == 1:
        if cnt == 1 or cnt == 0:
            return 0
        elif cnt >= 4:
            return 0
        elif cnt == 2 or cnt == 3:
            return 1

def encontrar(fila, columna):
    if fila < 0 or fila > tam-1 or columna < 0 or columna > tam-1:
        return None
    elif matriz[fila][columna] == 1:
        return 1
    else: 
        return 0


def simular():
    global matriz
    matriz_nueva = []
    for fil in range (0, tam):
        fil_nueva = []
        for col in range (0, tam):
            fil_nueva.append(vivir(fil, col, encontrar(fil, col)))
        matriz_nueva.append(fil_nueva)
    #print("----------------")
    #print(np.asarray(matriz_nueva))
    matriz = matriz_nueva
    #time.sleep(0.15)
    #plot()
    #print(np.asarray(matriz))
    """
    matriz2 = []
    
    for i2 in range(0,tam):
        fil = []
        for i in range (0,tam):
            if matriz[i2][i] == 1:
                fil.append(u"\u25A0")
            else:
                fil.append(	u"\u25A1")
        matriz2.append(fil)
    
    for i2 in range(0,tam):
        val = "".join(matriz2[i2])
        print(val)
    """
    print(np.asarray(matriz))
    


def plot():
    global matriz
    plt.imshow(np.asarray(matriz))
    plt.show()

    
t_i = time.time()
for i in range(0, ejecuciones):
    print(i)
    print (u"\u2589")
    #plot()
    time.sleep(0.15)
    simular()
    

print("tiempo ejecución:", time.time()-t_i)
input()