def all_permutations_of_letters(word):
    if type(word)==str:
        word = list(word) #hacemos la palabra una lista
        permutations = [""] #creamos la lista de permutaciones
        while len(permutations[0])<len(word): #mientras el primer elemento de las permutaciones no tenga igual cantidad que la palabra
            additions = [] #creamos una variable que guarde lo añadido
            for element in permutations: #para cada elemento de las permutaciones
                rest = [] #creamos lo que nos falta
                for letter in word: #si una letra en la palabra
                    if element.find(letter)==-1: #no está en el elemento
                        rest.append(letter) #lo añade
                additions+=[element+j for j in rest] #ahora agregamos a additions el elemento más otra letra que no tenga
            permutations = additions.copy() #ahora las permutaciones son estas
        return permutations
print(all_permutations_of_letters("sol")) #lo ponemos a prueba
print(all_permutations_of_letters("12345"))
