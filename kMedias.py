import numpy as np

def kMedias(X,cantNeuronas):

    cantEntradas = len(X)
    tamFeatures = len(X[0])

    # 1- Inicialización: Se eligen k centroides con patrones al azar
    posCentroides = np.random.randint(0,cantEntradas,cantNeuronas)
    centroides = X[posCentroides]

    conjuntos = np.zeros(cantEntradas)

    maxIteraciones = 10000
    it = 0
    while it<maxIteraciones:
        reasignaciones = False

        # 2- Se reasignan los patrones al centroide mas cercano:
        for i in range(cantEntradas):
            distancias = np.zeros(cantNeuronas)
            for j in range(cantNeuronas):
                distancias[j] = np.linalg.norm(X[i][:]-centroides[j][:])
            centroideMin = np.argmin(distancias)
            if centroideMin != conjuntos[i]:
                reasignaciones = True
            conjuntos[i] = centroideMin

        # Si no hubo reasignaciones, corto
        if not reasignaciones:
            break

        # Calculo el tamaño de cada conjunto
        tamConjuntos = np.zeros(cantNeuronas)
        for i in range(cantNeuronas):
            valoresi = conjuntos == i
            tamConjuntos[i] = len(conjuntos[valoresi])
            # Para evitar la división por 0
            if tamConjuntos[i] == 0:
                tamConjuntos[i] = 1

        # Calculo los centroides
        for i in range(cantNeuronas):
            sumatoria = np.zeros(tamFeatures)
            for j in range(cantEntradas):
                if conjuntos[j] == i:
                    sumatoria += X[j][:]
            centroides[i][:] = sumatoria / tamConjuntos[i]

        it += 1

    return centroides
