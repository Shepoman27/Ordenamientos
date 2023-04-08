def mergesort(lista):
    if len(lista) <= 1:
        return lista
    
    # Dividimos la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad] #Guardamos el elemento izquierdo de la lista en una parte
    derecha = lista[mitad:] #Guardamos el elemento de la derecha de la lista en otra parte
    
    # Recursivamente ordenamos las dos mitades
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    
    # Combinamos las dos mitades ordenadas en una única lista ordenada
    return combinar(izquierda, derecha)

def combinar(izquierda, derecha):
    resultado = [] #Creamos una lista para guardar el resultado
    i, j = 0, 0 #Inicializamos indices para las sublistas izqauierdas y derechas
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    resultado += izquierda[i:]
    resultado += derecha[j:]
    
    return resultado

# Ejemplo de uso
lista = [4, 1, 8, 3, 9, 2, 5, 7, 6, 0]
ordenado = mergesort(lista)
print(ordenado)