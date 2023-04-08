
#Por selección
lista = [5,7,3,1,8,4,9,2,6] #Creamos la lista a ordenar
longitud = len(lista)  #Extraemos el tamaño de la lista
 



for i in range(longitud-1): #For para recorrer la lista
    
    menor = i
    
    for j in range(i+1,longitud): #For para vovler a recorrer la lista
        
        if lista[j] < lista[menor]: #Compára si un elemento de la lista es menor que los de la derecha
            
            menor = j #En caso de que si se guarda como un numvio menor
    
    temporal = lista[menor] #Se guarda la posicion del menor en una variables
    lista[menor] = lista[i] #Se hace el cambio de elementos del mayor a la derecha
    lista[i] = temporal #Y el menor se queda en la posicion del inicial
    
print(lista)





