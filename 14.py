# no pude encontrar los símbolos, tuve que reemplazarlos, pero pude resolver la lógica
# I couldn't find the corresponding symbols, so I had to replace them, but I could solve the logic part
spanish_to_aurebesh = { 
    "a":"🚂",
    "b":"🚃",
    "c":"🚄",
    "d":"🚅",
    "e":"🚆",
    "f":"🚇",
    "g":"🚈",
    "h":"🚉",
    "i":"🚊",
    "j":"🚝",
    "k":"🚞",
    "l":"🚋",
    "m":"🚌",
    "n":"🚍",
    "ñ":"🚎",
    "o":"🚐",
    "p":"🚑",
    "q":"🚒",
    "r":"🚓",
    "s":"🚔",
    "t":"🚕",
    "u":"🚖",
    "v":"🚗",
    "w":"🚘",
    "x":"🚙",
    "y":"🚚",
    "z":"🚛",
}
aurebesh_to_spanish = {v:k for k,v in spanish_to_aurebesh.items()} #construimos el diccionario inverso
def aurebesh_conversor(an_string):
    if type(an_string)==str:
        an_string = an_string.lower()
        an_string = list(an_string) #lo hacemos una lista
        for i in range(len(an_string)): #para cada letra
            if an_string[i] in list(spanish_to_aurebesh.keys()): #si es una letra del español
                an_string[i] = spanish_to_aurebesh[an_string[i]] #la cambia por su traducción
            elif an_string[i] in list(aurebesh_to_spanish.keys()): #si es un simbolo aurebush
                an_string[i] = aurebesh_to_spanish[an_string[i]] #lo cambia por su traducción
        return "".join(an_string) #junta todo y lo devuelve
        
print(aurebesh_conversor("Bendito Sea Dios"))
print(aurebesh_conversor(aurebesh_conversor("Bendito Sea Dios")))