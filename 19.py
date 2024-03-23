horizontal,vertical,right_down,up_right,right_up,down_right = "═","║","╗","╔","╝","╚" #nombramos estas variables así para facilitar la escritura del código
def print_spiral_from_lenght(lenght):
    if type(lenght)==int  and lenght>1: #solo actua si la longitud es mayor que 1, osea, de dos en adelante
        print(horizontal*(lenght-1)+right_down) #construimos la entrada de la espiral
        for i in range (1,lenght-1): #ahora construimos la parte de enmedio, de 1 hasta lengt -2, pues falta contar la parte de arriba y abajo
            if i<lenght//2: #si está en la primer mitad
                print(vertical*(i-1)+up_right+horizontal*(lenght-1-2*i)+right_down+vertical*i) #esta es la configuración
            elif i==lenght//2 and lenght%2==1: #en caso que haya un valor intermedio, cuando el lado es impar
                print(vertical*(lenght//2-1)+up_right+right_down+vertical*(lenght//2)) #ponemos este arreglo
            else: #en caso de la parte de abajo
                print(vertical*(lenght-1-i)+down_right+horizontal*(2*i-lenght)+right_up+vertical*(lenght-1-i)) #este es el arreglo
        print(down_right+horizontal*(lenght-2)+right_up) #finalmente dibujamos la parte de abajo
print_spiral_from_lenght(2) #vemos como quedan las primeras 10
print_spiral_from_lenght(3)
print_spiral_from_lenght(4)
print_spiral_from_lenght(5)
print_spiral_from_lenght(6)
print_spiral_from_lenght(7)
print_spiral_from_lenght(8)
print_spiral_from_lenght(9)
print_spiral_from_lenght(10)
print_spiral_from_lenght(11)
print_spiral_from_lenght(12)