def ordenamiento_seleccion(arr):
    n = len(arr)
    # Recorremos todo el arreglo
    for i in range(n - 1):
        # Suponemos inicialmente que el primer elemento de la porción es el menor
        minimo = i
        
        # Comparamos con el resto de los elementos hacia adelante
        for j in range(i + 1, n):
            if arr[j] < arr[minimo]:
                minimo = j  # Actualizamos el índice del nuevo mínimo encontrado
                
        # Si el mínimo encontrado no es el mismo que asumimos, hacemos el intercambio
        if minimo != i:
            arr[i], arr[minimo] = arr[minimo], arr[i]
            
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    datos = [25.4, 12.8, 35.1, 4.2, 18.5]
    print("Arreglo original:", datos)
    
    datos_ordenados = ordenamiento_seleccion(datos)
    print("Arreglo ordenado:", datos_ordenados)
