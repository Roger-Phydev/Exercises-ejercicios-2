from random import randint as rd
from random import choice # I imported what we need
# Let's define the questions:
questions = [
    ['En la saga zelda ¿Cuál juego de zelda salió en el año 2000?','ocarina of time','majoras mask','minish cap','wind waker','2'],
    ['¿En que juego de zelda apareció Ganondorf por primera vez?','zelda 1','a link to the past','wind waker','ocarina of time','4'],
    ['En breath of the wild de la saga zelda, existen muchas semillas kolog, ¿cuántas aproximadamente?','entre 100 y 150','entre 300 y 600','entre 800 y 900','más de 1000','3'],
    ['¿Cuál es la espada más simbólica de la saga the legend of zelda?','espada maestra','biggoron','espada kokiri','espada del guardián','1'],
    ['En la saga zelda ¿Las bombas sirven, aparte de como armas arrojadizas, para...?','abrir portales','conseguir armas','abrir zonas ocultas','invocar una deidad','3'],
    ['En la saga halo, ¿Cómo se llaman los villanos de la trilogía original?','covenant','final killers','troops','erasers','1'],
    ['En halo 4 ¿Cuáles de estos enemigos hacen su aparición por primera vez?','grunts','elites','hunters','knights','4'],
    ['En la saga halo, ¿Qué es un halo?','un enemigo','el jefe final','un arma muy poderosa','el protagonista','3'],
    ['En la saga halo, Arma icónica de la saga que no aparece en halo 2:','rifle de batalla','rifle de asalto','spnkr','rifle de plasma','2'],
    ['Cuando completas este juego de la saga halo NO aparece una escena especial','halo 2','halo 3','halo CE','halo infinite','1'],
    ['En la saga gears hay un personaje muy importante que se sacrifica en gears 3, ¿Quién es?','Dominic Santiago','Tai','Marcus Phoenix','August Cole','1'],
    ['El arma emblema de la saga gears of war tiene acoplada una...','lanza','espada','trituradora','motosierra','4'],
    ['En la saga gears of war hay un arma muy poderosa que solo se puede usar al aire libre con ayuda de satélites,¿Cuál es?','lancer','gnasher','martillo del alba','dropshot','3'],
    ['Durante gears 5, hay dos partes abiertas, ¿En qué biomas se basan?','selva y bosque','ninguno, son ciudades','estepa y desierto','bosque y montaña','3'],
    ['Nombre del enemigo principal en la saga gears of war','locust/larvas','alianza','federación','razors','1'],
    ['En los juegos de Mario, es el item principal:','champiñón','estrella','caparazón','hoja','1'],
    ['¿Cuál juego de mario se ambienta en el espacio?','Super mario 3','Super mario Space','Super mario galaxy','Super mario sunshine','3'],
    ['¿Cómo se llama el hermano de mario?','Luis','Luigi','Leandro','Lino','2'],
    ['En super mario 3, ¿Cuál item aparece menos?','estrella','champiñón','traje de tanuki','flor de fuego','3'],
    ['En super mario world, ¿Qué personaje comparte el protagonismo con Mario?','Toad','Luigi','Bowser','Yoshi','4'],
    ['Assasins Creed 2 se lleva a cabo en...','Italia','Francia','Egipto','Arabia','1'],
    ['Este título de Assasins creed se ambienta en la independencia de Estados Unidos:','Assasins creed 3','Assasins creed Origins','Assasins creed IV','Assasins creed Unity','1'],
    ['Arma emblema de la saga Assasins creed','hacha doble','hoja oculta','bastón','arco','2'],
    ['En la saga Assasins creed se usa mucho este deporte urbano','Parkour','Skate','BMX','Esgrima','1'],
    ['En la saga Assasins creed son los enemigos principales','Unión de bandidos','Orden de asesinos','Templarios','Tropas del miedo','3'],
    ['Juego de call of duty que toca la guerra de Vietnam','modern warfare','world at war','black ops','advanced warfare','3'],
    ['En minecraft, ¿cuál arma es la más emblemática?','Arco','Espada','Pico','Lanza','3'],
    ['En la saga Kirby, ¿Qué item te vuelve invencible momentaneamente?','paleta de caramelo','estrella','nuez','jugo de naranja','1'],
    ['En hi-fi rush, importa tener buen...','tino','ritmo','arma','tiempo','2'],
    ['¿Cuál juego de los siguientes NO es de rol?','Final Fantasy','Dragon quest','Starfield','Grim fandango','4']
]
# We define assets
door,unk,riddle,ghost,candies='🚪','⬜️','❓','👻','🍭'
items = [riddle,ghost]
def instrucciones()->None:
    print("Debes jugar eligiendo a donde ir, se te mostrará en pantalla tu juego. Deberás desplazarte y encontrar la sala de dulces")
    print("Dentro de cada habitación puedes encontrar:")
    print("🍭  Sala de dulces, finaliza el juego")
    print("🚪  Puerta, marca donde inicias la partida")
    print('⬜️  Sala aún sin abrir, debes ir hacia ella para saber que sala es')
    print('❓  Sala de enigma, para poder salir, debes responder una pregunta')
    print('👻  Sala de fantasmas, debes responder DOS preguntas para salir')
    print('Cuidado!!! Solo dispones de ciertos intentos según al dificultad: \nfácil-10 intentos \nnormal-5 intentos \ndifícil: 2 intentos')
def show_screen(scrn):
    for row in scrn:
        print(" "*40+"".join(row))
def play_in_screen_board(scrn,brd,x,y,num_attempt):
    scrn[x][y]=brd[x][y]
    if scrn[x][y]==door:
        show_screen(scrn)
        return [False,True]
    elif scrn[x][y]==riddle:
        show_screen(scrn)
        q = choice(questions) #select a random question
        print(f'{riddle}  {q[0]}')
        print(f'a) {q[1]}  b) {q[2]}')
        print(f'c) {q[3]}  d) {q[4]}')
        ans = input('Tu respuesta: ')
        while ans not in ['a','b','c','d']:
            ans = input('respuesta incorrecta, dime una respuesta válida')
        if ans == 'a':
            ans = '1'
        elif ans == 'b':
            ans = '2'
        elif ans == 'c':
            ans = '3'
        else:
            ans = '4'
        if ans == q[5]:
            print('Correcto')
            return [False,True]
        else:
            print(f"Incorrecto, respuesta correcta: {q[int(q[5])]}")
            num_attempt-=1
            print(f'intentos restantes: {num_attempt}')
            return [False,False]
    elif scrn[x][y]==ghost:
        show_screen(scrn)
        q = choice(questions) #select a random question
        print(f'{riddle}  {q[0]}')
        print(f'a) {q[1]}  b) {q[2]}')
        print(f'c) {q[3]}  d) {q[4]}')
        ans = input('Tu respuesta: ')
        while ans not in ['a','b','c','d']:
            ans = input('respuesta incorrecta, dime una respuesta válida')
        if ans == 'a':
            ans = '1'
        elif ans == 'b':
            ans = '2'
        elif ans == 'c':
            ans = '3'
        else:
            ans = '4'
        if ans == q[5]:
            print('Correcto')
        else:
            print(f"Incorrecto, respuesta correcta: {q[int(q[5])]}")
            num_attempt-=1
            print(f'intentos restantes: {num_attempt}')
            if num_attempt==0:
                return [False,True]
        q = choice(questions) #select a random question
        print(f'{riddle}  {q[0]}')
        print(f'a) {q[1]}  b) {q[2]}')
        print(f'c) {q[3]}  d) {q[4]}')
        ans = input('Tu respuesta: ')
        while ans not in ['a','b','c','d']:
            ans = input('respuesta incorrecta, dime una respuesta válida')
        if ans == 'a':
            ans = '1'
        elif ans == 'b':
            ans = '2'
        elif ans == 'c':
            ans = '3'
        else:
            ans = '4'
        if ans == q[5]:
            print('Correcto')
            return [False,True]
        else:
            print(f"Incorrecto, respuesta correcta: {q[int(q[5])]}")
            num_attempt-=1
            print(f'intentos restantes: {num_attempt}')
            return [False,False]
    elif scrn[x][y]==candies:
        show_screen(scrn)
        print('Ganaste, fin del juego')
        return [True,True]
def direccion(x,y):
    check = False
    while not check:
        q = input('Elige una opción válida para moverte: norte, sur, este, oeste')
        while q not in ['norte','sur','este','oeste']:
            q = input('opción NO válida, usa alguno de estos: norte, sur, este, oeste')
        if (q,x) in [('norte',0),('sur',3)]:
            print('no es posible moverse en esa dirección')
        elif (q,y) in [('este',0),('oeste',3)]:
            print(f'no es posible moverse en esa dirección')
        else:
            check = True
            if q == 'norte':
                x-=1
            elif q == 'sur':
                x+=1
            elif q == 'este':
                y-=1
            elif q == 'oeste':
                y+=1
    return (x,y)
instrucciones() #show intructions
ans = input('Elige que difucultad quieres: fácil, normal o difícil') #select difficult level
while ans not in ["fácil",'normal','difícil']:
    ans = input('opción NO válida, debe ser: fácil, normal o difícil')
if ans=='fácil':
    num_attempt = 10
elif ans=='normal':
    num_attempt = 5
else:
    num_attempt = 2#define the number of attempts
win=False #define this variable to know when is the game finished
screen = [['⬜️']*4 for i in range(4)] #we create the screen
board = [] #creates the board
for a in range(4): #generates the board randomly
    s = []
    for b in range(4): 
        s.append(choice([riddle,ghost]))
    board.append(s)
i,j=rd(1,2),rd(1,2)#generates the location of candy room
board[i][j]=candies
i,j=rd(0,3),rd(0,3) #generates door location
while (i in [1,2] and j in [0,1]) or (i in [0,3] and j in [1,2]):
    i,j = rd(0,3),rd(1,3)
screen[i][j]=door
board[i][j]=door
show_screen(screen)
while num_attempt!=0 and win==False:
    cont = False
    (i,j) = direccion(i,j)
    while not cont and num_attempt!=0:
        [win,cont] = play_in_screen_board(screen,board,i,j,num_attempt)
if num_attempt==0:
    print('fin de la partida: PERDISTE')