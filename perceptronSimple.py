import numpy as np

def perceptronSimple(X, yd):

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
    maxEpocas = 1000
    tol = 90
    for k in range(maxEpocas):
        for i in range(0, tamX): # Cantidad de pruebas
            y = np.dot(W, X[i][:])   #Calculo el y[i]
            if y > 0:
                y = 1
            else:
                y = -1
            #Actualizar pesos
            W = W + 0.1*(yd[i]-y)*X[i][:]

        # Comparo las salidas y calculo la cantidad de aciertos en una epoca

        tasaAcierto = 0
        for i in range(tamX): # Cantidad de pruebas
            y = np.dot(W, X[i][:])
            if y > 0:
                y = 1
            else:
                y = -1
            if y == yd[i]:
                tasaAcierto += 1
        tasaAcierto = (tasaAcierto/tamX)*100

        if(tasaAcierto > tol):
            break

    return W, tasaAcierto
