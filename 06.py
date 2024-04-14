r = "🗿"
p = "📄"
s = "✂️"
sp = "🖖"
l = "🦎"
def who_win(list_of_plays):
    if type(list_of_plays)==list: #los primeros 3 if serán filtros para verificar formatos
        a = True
        for element in list_of_plays: #para cada elemento
            if type(element)!=list or len(element)!=2: #si el elemento no es de tipo lista o no tiene longitud 2
                a = False #hacemos a Falso
        if a:
            b = True
            for element in list_of_plays:
                if not set(element).issubset({r,p,s,sp,l}): #si contiene elementos de fuera del establecido
                    b = False #hacemos a b falso
            if b:
                wins = [[s,p],[p,r],[r,l],[l,sp],[sp,s],[s,l],[sp,r],[r,s],[l,p],[p,sp]] #creamos una lista de las posibles victorias para el primer jugador
                #para lo anterior: tijeras corta papel, papel cubre piedra, piedra aplasta lagarto, lagarto envenena spock
                # spock destroza tijeras, tijeras decapita lagarto, spock vaporiza roca , roca destruye tijeras, lagarto debora papel y papel desautoriza spock
                stat = 0 #creamos una variable para saber quien va ganando
                for element in list_of_plays: #para cada jugada
                    if element in wins:#si gana el primer jugador
                        stat+=1 #sumamos uno
                    elif list(reversed(element)) in wins: #por el contrario, si gana el otro jugador(osea, si al voltear la lista es una victoria)
                        stat-=1 #restamos uno
                if stat>0: #si al final queda positivo
                    print("P1 wins") #gana el primer jugador
                elif stat<0: #si al final queda negativo
                    print("P2 wins") #gana el segundo jugador
                else:
                    print("Tie") #en el otro caso, es un empate
            else:
                print(f"Los elementos de tus sublistas solo pueden ser los siguientes: {r},{p},{s},{sp},{l}")
        else:
            print("Los elementos de tu lista deben se listas de solo dos elementos")
    else:
        print("El argumento debe ser una lista")
who_win("sdas") #no es una lista
who_win([[1],[3,4]]) #es lista, pero no todos sus sublistas tienen 2 elementos
who_win([1,3]) #es una lista pero no tiene sublistas
who_win([[1,2],[3,4]]) #es lista con sublistas de 2, pero no contienen caracteres válidos
who_win([[r,s],[r,l],[sp,s],[l,s],[sp,l],[p,s]])