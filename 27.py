import re
def get_excel_column_number(expression):
    if type(expression)==str and re.findall(r"[A-Z]+",expression)==[expression]: #si es un string y es una o más letras mayúsculas
        number = 0 #variable para saber el número
        expression = list(expression) #lo hacemos lista
        for i in range(len(expression)): #para cada indice
            number+= (ord(expression[i])-64)*26**(len(expression)-i-1) #sumamos su código ASCII menos 64 para que quede A=1,etc y multiplicamos por una potencia de 26 según su posición
        return number
print(get_excel_column_number("A"))
print(get_excel_column_number("Z"))
print(get_excel_column_number("AA"))
print(get_excel_column_number("CA")) #comprobamos que funciona