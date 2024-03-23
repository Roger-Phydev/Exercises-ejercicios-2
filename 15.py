import random
print("Bienvenido a piedra papel o tijeras")
print("Se jugarán tiradas a dos de tres")
points = 0 #aquí guardamos el puntaje
play = 0 #este cuenta las jugadas
while play<3 and abs(points)!=2: #mientras hayan menos de 3 jugadas y los puntos no beneficien a ninguno
    print(f"ronda {play+1}: Piedra(r),papel(p) o tijeras (s)...") #mostramos la ronda
    ans = input("elige una jugada: r,p o s\n") #ponemos las opciones
    while ans not in ["r","p","s"]: #mientras no haya una respuesta aceptable
        ans = input("error, tu respuesta solo puede ser r,p o s\n")
    machine = random.choice(["s","r","p"])
    if [ans,machine] in [["r","s"],["s","p"],["p","r"]]:
        print(f"{ans}  vs  {machine}: ganaste")
        points+=1 #sumamos en caso de victoria
        play+=1 #aumentamos el número de jugada
    elif [ans,machine] in [["s","r"],["r","p"],["p","s"]]:
        print(f"{ans}  vs  {machine}: perdiste")
        points-=1 #restamos en caso de derrota
        play+=1 #aumentamos el número de jugada
    else:
        print(f"{ans}  vs  {machine}: empate")#en caso de empate también lo mostramos, pero no aumentamos el número de jugadas
if points>0: #si hay puntos positivos
    print("Felicidades, Ganaste")
else:
    print("Lo siento, perdiste")
