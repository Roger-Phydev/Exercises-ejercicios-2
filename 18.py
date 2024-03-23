def is_prime(k):#creamos una función para saber si es primo
    d = 1
    while d<=k//2:#hacemos un ciclo que dura a lo más, la mitad de k
        if k%d==0 and d!=1: #si d divide a k 
            break #sale del ciclo
        d+=1
    if d==k//2+1:
        return True
    else:
        return False
print(is_prime(11))
def twin_primes_until(n):
    if type(n)==int and n>0:
        if n<5: #si n es inferior a 5, no regresa ningún primo gemelo
            return None
        else:
            twins = []
            for i in range(2,n-1): #revisamos solo para valores de 2 hasta n-2 (pues solo comprueba en pares i, i+2)
                if is_prime(i) and is_prime(i+2): #si el número i y dos arriba de él, también.
                    twins.append((i,i+2)) #agregamos la pareja a la tupla
            return twins
print(twin_primes_until(13)) #en efecto, hace lo que se pide
print(twin_primes_until(100))
