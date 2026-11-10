# Método de Ordenamiento por Selección

Este repositorio contiene una implementación en **Python** del algoritmo de ordenamiento por selección, junto con su respectivo pseudocódigo.

## ¿Cómo funciona?
El método de selección busca el elemento más pequeño de la lista y lo intercambia con el elemento de la primera posición. Luego, busca el segundo más pequeño y lo intercambia con la segunda posición, repitiendo el proceso secuencialmente hasta recorrer todo el arreglo.

## Pseudocódigo
```text
Algoritmo OrdenamientoPorSeleccion(A)
    n = longitud(A)
    Para i desde 0 hasta n - 2 hacer
        minimo = i
        Para j desde i + 1 hasta n - 1 hacer
            Si A[j] < A[minimo] entonces
                minimo = j
            Fin Si
        Fin Para
        Si minimo != i entonces
            Intercambiar A[i] con A[minimo]
        Fin Si
    Fin Para
Fin Algoritmo
