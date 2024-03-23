import re
def text_analysis(an_string):
    if type(an_string)==str:
        an_string = an_string.lower()
        words = re.findall(r"(?<=\s)[a-záéíóúñ]+|^[a-záéíóúñ]+",an_string) #creamos una lista con las palabras, las cuales solo tienen letras de la a-z con acento o ñ
        #además, si empieza la cadena con la palabra, también es válido
        phrases = an_string.split(".") #separamos usando el punto para obtener las frases
        l=0 #longitud media
        m = "" #palabra más larga
        for word in words: #un solo bloque iterativo
            l+= len(word)/(len(words)) #sumamos a l la longitud de cada palabra dividida entre el total de palabras
            if len(m)<len(word):
                m=word #actualizamos la palabra más larga
        print(f"Palabras: {len(words)}     Frases: {len(phrases)}")
        print(f"longitud promedio de palabra: {l}   Palabra más larga: {m}")
text_analysis("Me siento muy contento, me siento muy feliz. Pues yo creo, me voy a divertir. Oahhh, oahhhhhhhh")