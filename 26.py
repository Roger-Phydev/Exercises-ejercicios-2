import re
def abacus_read(list_of_rows):
    if type(list_of_rows)==list and len(list_of_rows)==7: #revisamos que la lista cumpla el formato
        conversion = 0 #creamos una variable para la conversión
        for i in range(len(list_of_rows)):#para cada elemento de la lista
            if type(list_of_rows[i])==str and list_of_rows[i].count("O")==9 and list_of_rows[i].find("---")!=-1 and len(list_of_rows[i])==12:
                #el formato debe ser, cada elemente debe ser str, debe tener 9 "O", debe contener "---" y la longitud debe ser 12 (9 "0" y 3 "-")
                conversion+= (len(re.findall(r".*(?=---)",list_of_rows[i])[0]))*10**(6-i) #lo anterior hace:
                #busca lo que esté antes de los ---, cuenta cauntos elementos tiene, y multiplica por la potencia de diez correspondiente
            else:
                print("error, tus filas deben ser 9 cuentas y 3 espacio de alambre, ejemplo: OOO---OOOOOO")
                return None
        return conversion #devolvemos la conversión
            
    else:
        print("error, el argumento debe se una lista de 7 elementos que contiene la configuración de las cuentas")
        return None
wrong_format = "OOO-OOOOO"
wrong_format_one  = ["23","f","10","ñ","LL","p","OOO"]
proof = ["O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO"] #usamos de prueba el ejemplo
abacus_read(wrong_format)
abacus_read(wrong_format_one)
print(abacus_read(proof))