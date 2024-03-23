"""
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
"""
""" brief previos explanation | breve explicación:

we're looking for triples (a,b,c) that satisfy c^2=a^2+b^2, where a,b,c are natural numbers. Anyway, we can
begin with c fixed and looking for a and b, but there are just two posibilities: a<=b or a>b, but that
doesn't matter because we can toogle the names "a" and "b" (if a>b => a<->b so now a=b and b=a => b>a) 
in order to choose always that b>=a. So we're just looking b>=a, but that implies 2b^2=b^2+b^2>=a^2+b^2=c^2, 
so b must be >=c/sqrt(2).In conclusión we just have to search b in the range [c/sqrt(2),c-1], because b=c 
implies a=0, not a triple. And then just check if a is an integer. Finally, because of c/sqrt(2) is always
an irrational number (because of c is integer) and we're looking just integers, we can use the function ceal. 
END

Estamos buscando tercias (a,b,c) tales que c^2=a^2+b^2, con a,b,c naturales. En cualquier caso, podemos 
empezar con c fijo y buscar los a y b, pero solo hay dos posibilidades: a<=b o a>b, pero eso no importa
porque podemos intercambiar las etiquetas "a" y "b" (si a>b => a<->b asi ahora a=b y b=a => b>a) para 
siempre elegir que b>=a. Así estamos buscando solo b>=a, pero eso implica que 2b^2=b^2+b^2>=a^2+b^2=c^2,
asi b debe ser >=c/raíz_cuadrada(2). En conclusión solo debemos buscar b en el intervalo [c/raíz_cuadrada(2),c-1]
porque b=c implica a=0, que no es una tercia. Y entonces solo verificar si a es un entero. Finalmente
como la cantidad c/raíz_cuadrada(2), siempre es un número irracional (al ser c un entero) podemos aplicarle
la función ceal (redondea hacia arriba). FIN
"""
from math import ceil
def pithagoric_triples_before(n: int)->list:
    if type(n)==int:
        triples = [] #creamos la lista vacía donde metemos las triadas
        if n<5: #para valores menores a cinco no hay ninguna
            print("no hay ninguno")
            return triples
        else:
            for c in range (5,n+1): #solo actúa para [5,n], pues a menos de 5 no hay tercias
                for b in range(ceil(c/(2)**0.5),c): # intervalo [c/sqrt(2),c-1]
                    a=(c**2 - b**2)**0.5 #calculamos a, we get a
                    if a.is_integer(): #si es entero
                        triples.append((int(a),b,c)) #introducimos el valor de la tercia
            return triples
    else:
        print("error, el argumento debe ser un entero")
pithagoric_triples_before("sds")
pithagoric_triples_before(4)
print(pithagoric_triples_before(5))
print(pithagoric_triples_before(20))