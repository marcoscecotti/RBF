import numpy as np
import math

def funcionRadial(X, medias,desvio, cantNeuronas):
    salidas = np.zeros((len(X), cantNeuronas))
    for i in range(len(X)):  # Para cada patron
        for j in range(cantNeuronas):
            arriba = -1 * np.sum((X[i] - medias[j]) ** 2)
            abajo = 2 * (desvio ** 2)
            todo = math.e ** (arriba / abajo)
            salidas[i][j] = todo # Para el patron i y la neurona j
    return salidas