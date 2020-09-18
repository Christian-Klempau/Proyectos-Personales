import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from random import choice
import numpy as np
from time import sleep
from threading import Thread, Lock


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGridLayout')
layout = QGridLayout()

def agregar(x, y, color):
    label = QLabel()
    if color:
        label.setStyleSheet("background-color: black;\nborder: 1px solid white")
    else:
        label.setStyleSheet("background-color: gray;\nborder: 1px solid white")
    layout.addWidget(label, x, y)
    return label

def cambiar(x, y, color):
    label = labels[y][x]
    if color:
        label.setStyleSheet("background-color: black")
    else:
        label.setStyleSheet("background-color: gray")
n = 80
t = 0.5
mat = []
labels = []

for x in range(0, n):
    fil = []
    fil_label = []
    for y in range(0, n):
        val = n - 1
        if x == val or x == 0 or y == val or y == 0:
            color = 0
        else:
            color = choice((0, 1))
        fil.append(color)

        label = agregar(x, y, color)
        fil_label.append(label)

    mat.append(fil)
    labels.append(fil_label)

mat = np.matrix(mat)

def simular():
    a = 0
    while True:
        sleep(t)
        a = 1 - a
        for x in range(1, n - 1):
            for y in range(1, 40):
                cambiar(x, y, choice((0, 1)))




layout.setSpacing(0)

window.setLayout(layout)

window.setFixedSize(n*10, n*10)
window.move(375, 0)

window.show()

sim = Thread(target=simular, daemon=True)
sim.start()

sys.exit(app.exec_())

