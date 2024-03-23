def missed_symbols(an_string,comparison_string):
    if type(an_string)==type(comparison_string)==str and len(an_string)==len(comparison_string): #solo actúa si tienen igual longitud y son str
        missed = [] #creamos la lista 
        an_string,comparison_string = list(an_string),list(comparison_string) #convertimos a listas
        for i in range(len(an_string)):
            if an_string[i]!=comparison_string[i]: #si son diferentes los caracteres
                missed.append(comparison_string[i]) #agregamos a la lista el caracter
        an_string,comparison_string = "".join(an_string),"".join(comparison_string) #devolvemos a su forma original cada variable
        return missed #devolvemos la lista de caracteres
print(missed_symbols("Me llamo mouredev","Me llemo mouredov")) #comprobamos con el ejemplo
print(missed_symbols("Me llamo.Brais Moure","Me llamo brais moure"))