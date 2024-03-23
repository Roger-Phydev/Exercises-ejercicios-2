coding = { #creamos un diccionario con la conversión
    "a":"4",
    "b":"l3",
    "c":"[",
    "d":")",
    "e":"3",
    "f":"|=",
    "g":"&",
    "h":"#",
    "i":"1",
    "j":",_|",
    "k":">|",
    "l":"7",
    "m":'/V\ ',
    "n":"^/",
    "o":"0",
    "p":"|*",
    "q":"(_,)",
    "r":"I?",
    "s":"5",
    "t":"+",
    "u":"(_)",
    "v":"\/",
    "w":"VV",
    "x":"><",
    "y":"`/",
    "z":"2",
    "1":"L",
    "2":"R",
    "3":"E",
    "4":"A",
    "5":"S",
    "6":"b",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"o"
}
def to_hacker(an_string):
    if type(an_string)==str:
        an_string = an_string.lower() #hacemos todo en minúsculas para facilitar
        an_string = list(an_string) #lo convertimos a lista
        l = list(coding.keys())#una lista con los alfanuméricos
        coded = ""
        for letter in an_string: #para cada letra
            if letter in l: #si está en la lista
                letter = coding[letter]#lo cambiamos por su equivalente
            coded+=letter #en cualquier caso, sumamos la expresión a la variable coded
        return coded #devolvemos la cadena resultante
a =  "RogEr1 Parra"
print(a)
print(to_hacker(a))