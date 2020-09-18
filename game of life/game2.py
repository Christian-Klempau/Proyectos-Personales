import numpy as np
import sys
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

tam = 250
np.random.seed(42)
arr = np.random.randint(2, size=(tam, tam))

arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
#print(arr)
n_max = 100


def vecinos(arr, y, x):
    cnt = 0
    # * linea arriba
    for yi in range(y-1, y+2):
        if arr[yi, x-1] == 1:
            cnt += 1
    # * linea misma, excluirse
    for yi in range(y-1, y+2):
        if arr[yi, x] == 1 and (yi != y):
            cnt += 1
    # * linea abajo
    for yi in range(y-1, y+2):
        if arr[yi, x+1] == 1:
            cnt += 1

    return cnt

def simular():
    global tam
    global arr
    t0 = time.time()
    arr_copia = arr.copy()
    for yi in range(1, tam+1):
        for xi in range(1, tam+1):
            cnt = vecinos(arr_copia, yi, xi)
            val = arr[yi, xi]

            if cnt < 2 and val:
                arr[yi, xi] = 0
            elif cnt > 3 and val:
                arr[yi, xi] = 0
            elif cnt == 3 and not val:
                arr[yi, xi] = 1
    tiempos.append(time.time() - t0)
    return arr

    #global tam
    #nuevo_arr = np.random.randint(2, size=(tam, tam))
    #nuevo_arr = np.pad(nuevo_arr, pad_width=1, mode='constant', constant_values=0)
    # [y, x]
    #nuevo_arr[1, 3] = 7

tiempos = []
n = 0
def updatefig(*args):
    global n
    n += 1
    if n == n_max:
        salir()
    arr_actual = simular()
    im = plt.imshow(arr_actual, animated=True)
    im.set_array(arr_actual)
    return im,


def salir():
    print(max(tiempos), min(tiempos))
    print(sum(tiempos)/len(tiempos))
    sys.exit()


fig = plt.figure()
ani = animation.FuncAnimation(fig, updatefig,  blit=True)
plt.show()
