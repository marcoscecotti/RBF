import math
import random
import matplotlib.pyplot as plt
import numpy as np

def kMedias(X, cantNeuronas, graficar):
    # Definimos
    centroides = []
    centroidesAnt = np.zeros((cantNeuronas, len(X[0])))
    n = len(X)
    conjuntos = np.random.choice(cantNeuronas, n).transpose()

    # Definimos centroidesRandom
    for i in range(cantNeuronas):
        indice = random.randint(0, n-1)
        centroides.append(X[indice])

    # Grafico inicial
    if graficar:
        plt.title('kMedias')
        plt.xlabel("X1")
        plt.ylabel("X2")

        # Graficamos los iniciales
        for i in range(cantNeuronas):
            promLargo = (centroides[i][0] + centroides[i][1]) / 2
            promAncho = (centroides[i][2] + centroides[i][3]) / 2
            plt.scatter(promAncho, promLargo, marker='*', c='red')

    # whileamo
    cambioCentroide = True
    while cambioCentroide:
        cambioCentroide = False

        # Para todas los patrones, buscamos el menor centroide
        for i in range(n):  # Para cada patrón
            distCentroide = math.dist(X[i], centroides[0])
            indiceMenorCentroide = 0
            for j in range(1, cantNeuronas):  # Cada centroide
                distAux = math.dist(X[i], centroides[j])
                if distCentroide > distAux:
                    distCentroide = distAux
                    indiceMenorCentroide = j
            conjuntos[i] = indiceMenorCentroide

        # En este punto tengo actualizados mis nuevos conjuntos BIEN

        # Actualizar centroides
        for j in range(cantNeuronas):
            sumaCentroide = np.zeros(len(X[0]))
            cantCentroide = 0
            for i in range(n):  # Todos los patrones
                if conjuntos[i] == j:
                    sumaCentroide = sumaCentroide + X[i]
                    cantCentroide = cantCentroide + 1
            # Promedio
            for i in range(len(sumaCentroide)):
                if cantCentroide==0:
                    cantCentroide = 1
                centroides[j][i] = sumaCentroide[i] / cantCentroide

            # Me fijo si cambió, y lo reasigno
            if (centroides[j] != centroidesAnt[j]).any():
                cambioCentroide = True
                centroidesAnt[j] = centroides[j]

    if graficar:
        vColor = ["yellow", "blue", "black", "violet", "brown", "purple", "pink", "grey", "cyan", "orange"]
        for i in range(n):
            promLargo = (X[i][0] + X[i][1]) / 2
            promAncho = (X[i][2] + X[i][3]) / 2
            plt.scatter(promAncho, promLargo, marker='+', c=vColor[conjuntos[i]])

        for i in range(cantNeuronas):
            promLargo = (centroides[i][0] + centroides[i][1]) / 2
            promAncho = (centroides[i][2] + centroides[i][3]) / 2
            plt.scatter(promAncho, promLargo, marker='*', c='green')

        plt.show()
    return centroides