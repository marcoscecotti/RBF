# Red neuronal con funciones de base radial - Método de k-medias

Algoritmo de entrenamiento no supervisado con un método de k-medias para una red neuronal con funciones de base radial.

El script prueba_Xor_Iris realiza un entrenamiento no supervisado con k-medias y funciones de base radial, para luego con esas neuronas entrenar la última capa de un
perceptrón simple o multicapa, dependiendo de la cantidad de clases de salida. 
Además se realiza un entrenamiento con un perceptrón multicapa para comparar las velocidades de ejecución de ambos algoritmos y su tasa de acierto.

Para el conjunto de datos XOR, se grafica la distribución de los datos y cómo se ajustan los centroides por el método de k-medias:

![Image text](https://github.com/marcoscecotti/RBF/blob/main/datos/k-medias.png)

El script prueba_merval utiliza el método de k-medias para hacer regresión, en el cual se estima el valor del merval teniendo en cuenta 5 días anteriores. Se grafica la gráfica con los datos originales y con los datos aproximados obtenidos con k-medias y perceptrón simple, junto con la disminución del error cuadrático:

![Image text](https://github.com/marcoscecotti/RBF/blob/main/datos/prueba_merval.png)
