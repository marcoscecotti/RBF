import numpy as np

def test(xTest, ydTest,W):
    tamxTest = len(xTest)

    # Columna -1
    columnAux = (np.full((tamxTest, 1), -1))
    xTest = np.hstack((columnAux, xTest))

    #Comparo las salidas y calculo la cantidad de aciertos en una epoca
    acierto = 0
    for i in range(tamxTest):
        y = np.dot(W, xTest[i][:])
        if y > 0:
            y = 1
        else:
            y = -1
        if y == ydTest[i]:
            acierto += 1

    tasaAcierto = (acierto / tamxTest)*100
    return tasaAcierto