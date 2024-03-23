converter = {
    "1":[",",".","?","!"],
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"]
}
import re
def t9_conversor(code):
    if type(code)==str and re.findall(r"[1-9]{1,4}(?!>-)",code)==code.split("-"): #si es una cadena y al partirlo usando - quedan las coincidencias con números de a lo más 4 digitos
        code = code.split("-") #lo separamos por el -
        conversion = "" #creamos una variable para la conversión
        for element in code:
            if element[0] not in ["1","7","9"] and len(element)==4: #si se pulsan 4 veces algo distinto a 1,7 o 9
                print("los únicos números que admiten 4 pulsaciones son 1, 7 y 9") #informamos del error
                return None
            if element.count(element[0])!=len(element): #si no esta conformado por un solo número
                print("solo debe pulsarse un número una o más veces seguidas antes de un guio: 333-1 correcto |  332-1 incorrecto")
                return False
            conversion+=converter[element[0]][element.count(element[0])-1] #si supera las condiciones, añadimos el caracter según la cantidad de pulsaciones
        else:
            return conversion #en caso de acabar el for, regresa la conversión
    else:
        print("tu entrada deben ser grupos con, una a cuatro pulsaciones de número y un guion, salvo el último, ejemplo: 22-3")
        return False
    
print(t9_conversor("6-666-88-777-33-3-33-888")) #probamos el ejemplo
print(t9_conversor("22-777-444-2-66-7-2-777-777-2"))
