def print_triforce(length):
    if type(length)==int and length>0:
        for i in range(2*length):
            if i<length:
                print(" "*(2*length-i)+"*"*(2*i+1))#pintamos el primer triangulo
            else: #luego pintamos el segundo y tercer tríangulo
                print(" "*(2*length-i)+"*"*(2*(i-length)+1)+" "*(4*length-2*i-1)+"*"*(2*(i-length)+1))
print_triforce(2)
print_triforce(3)
print_triforce(5) #en efecto, pinta lo que queremos