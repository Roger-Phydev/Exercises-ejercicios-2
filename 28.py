def all_permutations_of_letters(word):
    if type(word)==str:
        permutations = [""] #creamos la lista de permutaciones
        while len(permutations[0])<len(word): #mientras el primer elemento de las permutaciones no tenga igual cantidad que la palabra
            additions = [] #creamos una variable que guarde lo añadido
            for element in permutations: #para cada elemento de las permutaciones
                rest = list(word) #usaremos esto para los que nos falta
                for i in range(len(element)) : #recorremos indices del elemento
                    rest.remove(element[i]) #quitamos lo que esté presente en el elemento
                additions+=[element+j for j in rest] #ahora agregamos a additions el elemento más otra letra que no tenga
            permutations = additions.copy() #ahora las permutaciones son estas
        return permutations
print(all_permutations_of_letters("ella")) #lo ponemos a prueba
print(all_permutations_of_letters("sol"))
