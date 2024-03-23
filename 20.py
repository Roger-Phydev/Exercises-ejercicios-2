#Breve resumen, el cifrado césar desplaza una cantidad fija de lugares cada letra del abecedario
#Por ejemplo: si tomamos 2 espacios, la A se vuelve una C
def caesar_coding(an_string,uncode=False,space=4): #creamos la función, pudiendo elegir si descifrar o no (por default, no), y los espacios (por default 4)
    if type(an_string)==str:
        an_string = list(an_string) #lo volvemos una lista
        if uncode==False: #en caso de no querer decodificar, codificamos            
            for i in range(len(an_string)):
                if ord(an_string[i]) in range(65,91): #si se encuentra en mayúsculas
                    an_string[i] = chr(65+(ord(an_string[i])-65+space)%26) #sumamos la cantidad de espacios y realizamos módulo para dar la vuelta
                elif ord(an_string[i]) in range(97,123): #si es minúscula, hacemos lo propio
                    an_string[i] = chr(97+(ord(an_string[i])-97+space)%26)
            an_string = "".join(an_string) #pegamos de nuevo la cadena
            return an_string #y la devolvemos
        elif uncode==True: #si quiere decodificarse
            for i in range(len(an_string)):#repetimos el proceso
                if ord(an_string[i]) in range(65,91): 
                    an_string[i] = chr(65+(ord(an_string[i])-65-space)%26) #solo que ahora restamos la cantidad de espacios
                elif ord(an_string[i]) in range(97,123): 
                    an_string[i] = chr(97+(ord(an_string[i])-97-space)%26)
            an_string = "".join(an_string) 
            return an_string 
proof = "".join([chr(65+i) for i in range(26)]) #creamos la prueba con mayúsculas
print(proof,caesar_coding(proof),caesar_coding(proof,True)) #ahora revisamos que codifique y descodifique bien
proof = proof.lower() #ahora revisamos que pasa con las minusculas
print(proof,caesar_coding(proof),caesar_coding(proof,True))
print(caesar_coding("Que bonito dia 1234.;:",space=2),caesar_coding(caesar_coding("Es muy facil",space=3),True,3)) #ahora vemos que pasa con diferentes espacios
#a la vez que como al codificar y descodificar queda igual, igual los números no los cambia