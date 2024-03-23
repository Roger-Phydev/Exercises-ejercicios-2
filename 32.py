"""
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
"""
def mult_tables(n:int)->None:
    if type(n)==int and n>0 and n<11:
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")
    else:
        print("Error: debe introducir un número entero de 1 a 10")
mult_tables(7)