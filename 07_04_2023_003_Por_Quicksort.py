#Algoritmos de ordenamiento
#Por Quicksort
def quicksort(lista):
    # Si la lista tiene longitud 0 o 1, ya está ordenada y se devuelve tal cual.
    if len(lista) <= 1:
        return lista
    else:
        # Se elige un elemento "pivot" (en este caso, el primer elemento).
        pivot = lista[0]
        # Se divide la lista en dos: una con los elementos menores o iguales al pivot...
        menores = [x for x in lista[1:] if x <= pivot]
        # ... y otra con los mayores.
        mayores = [x for x in lista[1:] if x > pivot]
        # Se llama recursivamente a la función quicksort() para ordenar las dos listas de elementos menores y mayores...
        return quicksort(menores) + [pivot] + quicksort(mayores)

# Ejemplo de uso:
lista = [4, 8, 2, 1, 7, 5, 6, 3, 9]
# Se llama a la función quicksort() pasándole la lista de números a ordenar como argumento.
print(quicksort(lista))