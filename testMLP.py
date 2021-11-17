import math

import numpy as np

def testIris(X,yd,W,capas,ejercicio):
    cantCapas = len(capas)

    cantPruebas = len(X)
    cantEntradas = len(X[0])
    # Le agrego la entrada -1 correspondiente al BIAS (umbral / parcialidad)
    columnBIAS = (np.full((cantPruebas, 1), -1))
    X = np.hstack((columnBIAS, X))  # reagrupamos

    # Comparo las salidas y calculo la cantidad de errores en una epoca
    e = math.e
    b=1
    acierto = 0
    for i in range(cantPruebas):
        yCapaBIAS = []
        yCapaBIAS.insert(0, X[i][:].tolist())  # Insertamos las entradas
        for j in range(cantCapas):
            yAux = []
            Xt = np.transpose(yCapaBIAS[j][:])
            V = np.dot(W[j][:][:], Xt)
            for k in range(len(V)):
                sigmoide = (2 / (1 + e ** (-b * V[k]))) - 1
                yAux.insert(k, sigmoide)
            yAux.insert(0, -1)
            yCapaBIAS.insert(j + 1, yAux)
        if ejercicio == 1:
            y = yCapaBIAS[cantCapas][1]  # Salida final
            # Funcion signo
            if y > 0:
                y = 1
            else:
                y = -1

            if y == yd[i]:
                acierto += 1
        if ejercicio == 2:
            y = yCapaBIAS[cantCapas][:]  # Salida final

            # Regla de y
            y = np.array(y[1:])
            index = np.unravel_index(y.argmax(), y.shape)
            for l in range(len(y)):
                y[l] = -1
            y[index] = 1

            cont = 0
            for m in range(len(y)):
                if y[m] != yd[i][m]:
                    cont += 1

            if cont == 0:
                acierto += 1
    tasaAcierto = (acierto / cantPruebas) * 100
    return tasaAcierto