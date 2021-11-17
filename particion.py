import numpy as np

def particion(df,porcentajeTest):
    cantPruebas = len(df)
    indices = np.random.choice(cantPruebas,cantPruebas,replace=False)
    indicesTrain = indices[:int(cantPruebas*(1-porcentajeTest))]
    indicesTest = indices[int(cantPruebas*(1-porcentajeTest))+1:]
    return indicesTrain,indicesTest
