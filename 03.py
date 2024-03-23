import random
def random_password(lenght,upper=False,numbers=False,symbols=False):
    if type(lenght)==int and lenght<=16 and lenght>=8:
        choices = list("abcdefghijklmnopqrstuvwz") #creamos una lista con letras minúsculas de la que eligiremos
        if upper==True:
            choices+=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #si quiere mayúsculas, agregamos a la lista las mayúsculas
        if numbers==True:
            choices+=list("1234567890") #agregamos los números
        if symbols==True:
            choices+=list("!#$%&/()=?¡*][¨{-_}^+|°¬") #agregamos los símbolos especiales
        password = ""
        for i in range(lenght):
            password+=random.choice(choices) #agregamos los elementos
        return password
print(random_password(19)) #aqui no hace nada al no se de la longitud adecuada
print(random_password(10)) #solo tiene letras minúsculas
print(random_password(12,True)) #mayúsculas y minúsculas
print(random_password(14,True,True))#letras y números
print(random_password(8,True,True,True)) #alfanuméricos y especiales