numeros = [1,5,3,2]
objetivo = 6
def combinations_sum_objetive(numbers_list:list,objetive:int)->list:
    numbers_list.sort() #ordenamos
    numbers_list.reverse() #invertimos, quedando la lista en forma descendente, lo que mejora la eficiencia del código
    combinations = []
    posibilities = [[]] #creamos una lista de posibilidades 
    for element in numbers_list: #para cada elemento de los números
        posibilities+= [posibility+[element] for posibility in posibilities] #añadimos a lo que ya tiene, los mismos elementos pero pegandole el elemento al final
        for posibility in posibilities: #ahora escrutamos la lista de posibilidades
            if sum(posibility)>objetive: #si la suma supera al objetivo
                posibilities.remove(posibility) #remueve el elemento
            elif sum(posibility)==objetive: #si justo suma el objetivo
                if posibility not in combinations: #y además no está entre las combinaciones:
                    combinations.append(posibility) #lo añade
                posibilities.remove(posibility) #independientemente de si está o no, lo quita de las posibilidades
            #lo anterior sirve para reducir la longitud de posibilities y reducir la cantidad de escrutinio
    posibilities.remove([]) #después quitamos el vacío que solo servía para construir el conjunto de posibilidades
    return combinations #regresamos lo solicitado
print(combinations_sum_objetive(numeros,objetivo)) #vemos que cumpla con el ejemplo
print(combinations_sum_objetive([1,2,3,4,5,5,5,5],10)) #aqui vemos que no importa si hay varias repeticiones, no alter la lista
print(combinations_sum_objetive([1,5],4))#si no es posible, regresa vacío
print(combinations_sum_objetive([1,2,1,1,2,2],2))
