lista = [4,5,7,6,3,1,9,8,2]

band = False
while band == False: #Un while, mientras este desordenado se repetira el ciclo
    band = True
    for i in range(len(lista)-1):
        if lista[i]> lista [i+1]: #Si el elemnto de la derecha es menor
            aux = lista[i] #Se guarda el elemento actual en una variable
            lista[i] = lista[i+1]#Ahora El elemento a comparar será el de la derecha
            lista[i+1] = aux  
            band = False
            
print(lista)
    