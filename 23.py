import re
def is_correct_math_expression(expression):
    if type(expression)==str: #solo si es una cadena se ejecuta
        expression = expression.split(" ") #separmos usando los espacios
        if len(expression)<3: #si hay menos de 3 caracteres, no es posible que sea correcto
            return False
        for i in range(len(expression)):
            if i%2==0 and not expression[i].isnumeric(): #si es indice par y no es un número
                return False #devuelve falso
            elif i%2==1 and expression[i] not in ["*","/","+","-"]: #en caso de ser impar y no ser un símbolo de operación
                return False #devuelve falso
        else: #en caso de que termine el for
            return True #devuelve verdadero
print(is_correct_math_expression("5 a"))#ponemos a prueba el programa
print(is_correct_math_expression("5 a 6"))
print(is_correct_math_expression("5 + 6 / 7 - 4"))