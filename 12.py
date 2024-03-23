import random
print("Bienvenido a ADIVINA LA PALABRA")
print("deberás adivinar la palabra incompleta. Puedes en cada intento introducir una intento de adivinar la palabra completa")
print("O puedes introducir solo una letra")
n = 0
dif = 0
while n not in [5,10,15]:
    n = int(input("¿Cuantos intentos quieres tener?\n5(difícil)  10(normal)  15(fácil)\n")) #seguimos preguntando hasta obtener una respuesta válida
while dif not in ["1","2","3"]:
    dif = input("Selecciona una dificultad: 1(fácil) 2(normal) 3(difícil)\n")
word = random.choice(["ventilador","favorito","murcielago","dormitorio","armadillo","violencia","videojuego","computadora","ornitorrinco","camaraderia"]) #elige una palabra
if dif == "1":
    dif = len(word)//8 #en caso fácil, solo se ocultará a lo más un octavo
if dif == "2":
    dif = len(word)//3 #en normal, a lo más un tercio
if dif == "3":
    dif = len(word)//2+1 #en normal, cerca de la mitad
show_word = list(word) #esta será la palabra mostrada
solution = [] #esto contendrá la solución
positions = [] #y esta será la posición a cambiar correspondiente
while len(solution)<dif: #mientras no haya dif letras borradas, aparecerá lo siguiente:
    select = random.choice(range(len(word))) #escogemos un indice en la palabra
    if show_word[select]!="_": #si lo que aparece no es un _
        solution.append(show_word[select]) #agregamos la letra a la solución
        show_word[select] = "_" #cambiamos el lugar por un _
        positions.append(select) #y agregamos el índice a la posicion
vict = False
while vict==False and n>0: #mientras no haya ganado o aun queden intentos
    print("Palabra secreta: ",end="")
    for element in show_word:
        print(f"{element}",end="")
    turn = input(f"\nIntroduce una letra o intenta adivinar la palabra                                        Intentos:{n}\n") #señalamos los intentos y damos instrucciones
    while len(turn)!=1 and len(turn)!=len(word): #mientras la longitud de lo introducido no sea 1 (una sola letra) o coincida con word (un intendo de adivinar)
        print("Debes introducir solo una letra, o intentar adivinar(debe contener la misma cantidad de letras que la palabra secreta)\n")
        turn = input("\nIntroduce una letra o intenta adivinar la palabra")
    if turn == word: #si coincide con la palabra
        vict=True #ya ganó
    elif turn in solution: #si está entra la solución
        i = solution.index(turn) #obtenemos su indice
        show_word[positions.pop(i)]=solution.pop(i) #cambiamos el _ por su correspondiente letra y borramos la entrada
    else:
        n-=1 #en caso que falle, restamos un intento
    if len(solution)==0: #si después de eso, ya no queda nada en solution
        vict = True #es porque ganó
    
if vict==True:
    print(f"Felicidades:     palabra secreta: {word}     intentos sobrantes:{n}") #si ganó, mostramos la palabra y cuantos intentos le quedaron
elif vict==False:
    print(f"Lástima, se te terminaron los intentos.       Palabra secreta:{word}") #en caso de derrota, mostramos solo la palabra

    