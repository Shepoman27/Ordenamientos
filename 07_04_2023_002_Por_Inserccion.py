#Algoritmos de ordenamiento
#Por insercción

lista = [5,7,3,1,8,4,9,2,6]

longitud = len(lista)

for i in range (1,longitud): #Recorremos la lista
    
    actual = lista[i] #Gurdamos en una variable el elemento actual
    indice = i #Creamos una variable que guarde la posicion i
    
    while indice > 0 and  lista[indice-1]> actual:#Mientras indice se mayor que 0 y el elemeento de la derecha sea mayor que la posicion actual de la liusta en i
        lista[indice] = lista[indice-1] #Se guarda dicho elemento en indice actual
        indice = indice -1 #Se le resta 1 a indice para comparar con otro elemento
        
    lista[indice] = actual #Se guarda el valor actual en la posicion indice
        
print(lista)