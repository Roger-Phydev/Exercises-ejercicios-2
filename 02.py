def tennis_sequence(number_one,number_two):

    if number_one=="Love": #avanzamos en cada caso
        return "15"
    elif number_one=="15":
        return "30"
    elif number_one=="30" and number_two!="40":#lo mismo pero sin el 40 porque iría a empate
        return "40"
    elif number_one == "30" and number_two=="40": #si el primero es 30 y el otro cuarenta
        return "deuce"        #y regresamos empate
    elif number_one=="40" and number_two=="advantage": #si el segundo tiene ventaja y el primero tenía 40
        return "deuce"
    elif number_one=="deuce":
        return "advantage"
    elif number_one=="40" and number_two!="advantage": #si se tiene un 40 en primer lugar, como ya quitamos el caso de advantage
        return "advantage" #tendrá ventaja
    elif number_one=="advantage":
        return "win"
def tennis_match(a_list):
    if type(a_list)==list and len(a_list)==a_list.count("P1")+a_list.count("P2"):
        state_p_one = "Love" #creamos variables del marcador
        state_p_two = "Love"
        for element in a_list:
            if element=="P1" and state_p_one!="win" and state_p_two!="win": #siempre que se seleccione a P1 y no haya ganado nadie
                state_p_one = tennis_sequence(state_p_one,state_p_two) #movemos en secuencia el marcador de P1
                if state_p_one=="advantage": #si va ganando P1
                    state_p_two="40"
                    print(f"P1 {state_p_one}") #lo señalamos
                elif state_p_one=="deuce": #si hay un empate
                    state_p_two="deuce"
                    print(f"{state_p_one}")
                elif state_p_one=="win":
                    print("P1 wins")#si el jugador uno gana, lo muestra
                else:
                    print(f"{state_p_one} - {state_p_two}") #mostramos el marcador 
            if element=="P2" and state_p_two!="win" and state_p_one!="win":
                state_p_two = tennis_sequence(state_p_two,state_p_one) #movemos en secuencia el marcador de P1
                if state_p_two=="advantage": #si va ganando P1
                    state_p_one="40" #regresamos el estado del otro a 40
                    print(f"P2 {state_p_two}") #lo señalamos
                elif state_p_two=="deuce": #si hay un empate
                    state_p_one="deuce" #el otro se actualiza al empate
                    print(f"{state_p_two}")
                elif state_p_two=="win":
                    print("P2 wins")#si el jugador uno gana, lo muestra
                else:
                    print(f"{state_p_one} - {state_p_two}") #mostramos el marcador 
    else:
        print("el argumento debe ser una lista, y solo debe incluir alguna de las expresiones: P1 o P2")
tennis_match("sdsad") #no es lista
tennis_match([1,2,1]) #no incluye P1 o P2
tennis_match(["P1",2,2]) #no incluye SOLO P1 y P2
tennis_match(["P1","P1","P2","P2","P1","P2","P1","P1"])
tennis_match(["P1","P1","P1","P2","P2","P2","P2","P1","P1","P1","P1","P2","P2","P2"]) #aquí después de que ganó P1 añadimos muchos P2, pero aún así la victoria se conserva para P1
tennis_match(["P1","P2","P1","P1","P2","P2","P1","P2","P2","P2","P1"]) #comprobamos que pueda volver a deuce