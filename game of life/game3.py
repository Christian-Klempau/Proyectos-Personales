import numpy as np
import sys
import time
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation

tam = 250
np.random.seed(42)
arr = np.random.randint(2, size=(tam, tam))
#arr = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
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
    t0 = time.time()
    arr_copia = arr.copy()
    threads = []
    for yi in range(1, tam+1):
        t = threading.Thread(target=fila, args=(arr_copia[yi], arr_copia, yi))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    tiempos.append(time.time() - t0)
    #input()
    return arr


def fila(fila_arr, arr_copia, y):
    for xi in range(1, tam+1):
        cnt = vecinos(arr_copia, y, xi)
        val = fila_arr[xi]

        if cnt < 2 and val:
            fila_arr[xi] = 0
        elif cnt > 3 and val:
            fila_arr[xi] = 0
        elif cnt == 3 and not val:
            fila_arr[xi] = 1
        #print(cnt, val, fila_arr[xi])
    with lock:
        arr[y] = fila_arr
        #print (threading.currentThread().getName())
        


def updatefig(*args):
    global n
    global arr
    n += 1
    if n == n_max:
        salir()
    if n == 20:
        print(arr)
    arr = simular()
    im = plt.imshow(arr, animated=True)
    im.set_array(arr)
    return im,


def salir():
    print(max(tiempos), min(tiempos))
    print(sum(tiempos)/len(tiempos))
    sys.exit()

lock = threading.Lock()
tiempos = []
n = 0

fig = plt.figure()
ani = animation.FuncAnimation(fig, updatefig,  blit=True)
plt.show()
