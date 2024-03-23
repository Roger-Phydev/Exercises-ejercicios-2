import re
def is_heterogram(an_string):
    if type(an_string)==str : #solo actúa si es un str
        an_string = an_string.lower()
        l = re.findall(r"\s{0,1}[a-z]+[,.;:]{0,1}",an_string) #convertimos a lista con el patrón: espacios(1 o ninguno), una o más letras, signo de puntuación o ninguno
        letters = []
        for element in l: #quitamos los signos de puntuación y espacios
            for i in [" ",",",".",":",";"]:
                element = element.replace(i,"")
            letters+=list(element) #agregamos a la lista todo
        for i in range(len(letters)): #para cada índice
            if letters.count(letters[i])>1: #si el conteo de la letra correspondiente es mayor a 1 (osea que aparece 2 o más veces) se repite
                return False #en ese caso regresa False
        else:
            return True #en caso que termine el for, devuelve True
def is_isogram(an_string):
    if type(an_string)==str:
        an_string = an_string.lower()
        l = re.findall(r"\s{0,1}[a-z]+[,.;:]{0,1}",an_string) #convertimos a lista con el patrón: espacios(1 o ninguno), una o más letras, signo de puntuación o ninguno
        letters = []
        for element in l: #quitamos los signos de puntuación y espacios
            for i in [" ",",",".",":",";"]:
                element = element.replace(i,"",-1)
            letters+=list(element)
        m = letters.count(letters[0]) #contamos las veces que aparece la primera letra
        for i in range(len(letters)): #para cada índice
            if letters.count(letters[i])!=m: #si el conteo de la letra correspondiente es diferente al de la primera letra, no aparece cada letra igual cantidad de veces
                return False #en ese caso regresa False
        else:
            return True #en caso que termine el for, devuelve True
def is_pangram(an_string):
    if type(an_string)==str:
        an_string = an_string.lower() #convertimos a minúsculas
        l = re.findall(r"\s{0,1}[a-z]+[,.;:]{0,1}",an_string) #convertimos a lista con el patrón: espacios(1 o ninguno), una o más letras, signo de puntuación o ninguno
        letters = []
        for element in l: #quitamos los signos de puntuación y espacios
            for i in [" ",",",".",":",";"]:
                element = element.replace(i,"",-1)
            letters+=list(element) #y agregamos a las letras
        if set(letters)==set(list("abcdefghijklmnopqrstuvwxyz")):#si las letras son todo el abecedario
                return True #si es pangrama
        else:
                return False #en caso contrario regresa falso
print(is_heterogram("ale"))
print(is_isogram("alEela, "))#no cuenta espacio ni comas
print(is_pangram("asjf, saihdweiu"))
print(is_pangram("abcde, fghi. jklmnop: qrstu; vwxyz, siudierfer")) #este sí es un pangrama


