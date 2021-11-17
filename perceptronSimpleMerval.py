import numpy as np

def perceptronSimpleMerval(X, yd):

    tamX = len(X)
    tamAux = len(X[0])

    #Le agrego la entrada -1 correspondiente al BIAS (umbral / parcialidad)
    columnAux = (np.full((tamX,1), -1))
    X = np.hstack((columnAux, X)) # reagrupamos

    # Genero un vector de pesos aleatorios entre -0.5 y 0.5
    W = []
    for i in range(0, tamAux+1):
        W.insert(i, np.random.uniform(-0.5, 0.5))

    # Condiciones de corte
    maxEpocas = 100
    error = np.zeros(maxEpocas)
    for k in range(maxEpocas):
        for i in range(tamX): # Cantidad de pruebas
            y = np.dot(W, X[i][:])   #Calculo el y[i]
            #Actualizar pesos
            W = W + 0.01*(yd[i]-y)*X[i][:]

        # Calculo el error en cada epoca
        yAux = np.zeros(tamX)
        for i in range(tamX): # Cantidad de pruebas
            yAux[i] = np.dot(W, X[i][:])

        error[k] = np.linalg.norm(yd-yAux)

    return W, error, yAux
