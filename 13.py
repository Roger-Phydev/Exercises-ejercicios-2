def oct_and_hex(number):
    if type(number)==int:
        if number>=0: #si el número es positivo hacemos esto
            representation = ["",""]
            numbers = list("0123456789ABCDEF")#creamos una lista con símbolos
            for i in [0,1]:#para cada indice:
                n = number #iniciamos una variable con el valor del número
                while n>=1:
                    d = n%(8*(i+1)) #calculamos el residuo de dividir por 8 o 16
                    representation[i]=numbers[d]+representation[i] #añadimos el coeficiente correspondiente al inicio y no al final
                    n = (n-d)//(8*(i+1))#ahora a n le restamos el residuo y dividimos por 8o 16 y lo hacemos entero
            return representation
        else:
            return ["-"+oct_and_hex(-number)[0],"-"+oct_and_hex(-number)[1]] #si no, le aplicamos a su negativo y añadimos un signo menos
print(oct_and_hex(-123))
print(oct_and_hex(63)) #funciona adecuadamante