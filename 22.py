import time
def countdown(begin,last):
    if type(begin)==type(last)==int and begin>0 and last>0:
        pause = last/begin #el tiempo de pausa en cada caso será la duración entre el número en que inicia
        for i in range(begin+1):
            print(begin-i) #imprimimos
            i-=1
            time.sleep(pause) #paramos el tiempo según la pausa
    else:
        print("Tus datos deben ser números entero y positivos, el primero es el inicio, el segundo la duración en segundos")
countdown("l","34")
countdown(-10,1)
countdown(100,1)