def is_prime(n): #esta función determina si un número es primo
    if n == 1:
        return False #el 1 no es primo
    d = 1
    for i in range(2,n//2+1):
        if n%i==0:
            d+=1
    if d==1:
        return True
    else:
        return False
def fibonacci_until(l): #esta función devuelve la lista de los fibonacci menores o iguales a l
    secuence = [0,1,1] #la secuencia
    if l == 1:
        return secuence
    while secuence[-1]+secuence[-2]<=l: #mientras el valor siguiente no rebase a l
        secuence.append(secuence[-1]+secuence[-2])#aumentamos lo agregamos
    return secuence
def is_prime_fibonacci_odd(number):
    if type(number)==int and number>0:
        status = f"{number} "
        if is_prime(number): #si es primo
            status+="es primo, " #imprimimos esto sin saltar renglón
        else:
            status+="no es primo, "
        if number==fibonacci_until(number)[-1]: #si es igual al último elemento de la lista de fibonaccis menores o iguales a el número
            status+="es fibonacci y " #agregamos que es fibonacci
        else:
            status+="no es fibonacci y "
        if number%2==0:
            status+="es par" #agregamos que es par
        else:
            status+="es impar"
        return status #regresamos la cadena total
    else:
        print("error en tu entrada, debe ser un entero mayor que cero")
is_prime_fibonacci_odd(0) #aqui no funciona
print(is_prime_fibonacci_odd(2)) #aqui es primo, fib y par
print(is_prime_fibonacci_odd(5)) #aqui es primo, fib e impar
print(is_prime_fibonacci_odd(11)) #aqui es primo, no fib e impar
print(is_prime_fibonacci_odd(8)) # no es primo, es fib y par
print(is_prime_fibonacci_odd(21)) #no es primo, es fib e impar
print(is_prime_fibonacci_odd(9)) # no es primo, no es fib e impar
print(is_prime_fibonacci_odd(14)) #no es primo, no es fib es par
    