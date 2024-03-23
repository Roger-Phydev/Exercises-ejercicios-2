g = 0 #creamos una variable para guardar las respuestas correspondientes a cada casa
s = 0
h = 0
r = 0
print("Sombrero seleccionador de Hogwarths:")
print("Mago, responde las siguientes preguntas escribiendo el número correspondiente a la opción que elijas")
print("Estas en mitad de la noche y de repente una persona te ataca, tú...")
print("1.- te defiendes y luego contratacas")
print("2.- te defiendes y buscas ayuda")
print("3.- te defiendes y huyes")
print("4.- te defiendes y esperas a reconocer a la persona para decidir que hacer")
ans = 0
while ans not in ["1","2","3","4"]: #mientras la respuesta no sea válida
    ans = str(input("Selecciona tu respuesta (1-4): ")) #sigue preguntando
if ans == "1":
    g+=1
elif ans == "2":
    h+=1
elif ans == "3":
    r+=1
else:
    s+=1
print("Tienes una clase libre, ¿a dónde irías?")
print("1.- A entrenar tus hechizos y mejorar tus habilidades de combate")
print("2.- A reunirte con amigos y pasar un buen rato")
print("3.- A un laboratoria a mejorar tus conocimientos de alquimia")
print("4.- A divertirte sin más")
ans = 0
while ans not in ["1","2","3","4"]: #mientras la respuesta no sea válida
    ans = str(input("Selecciona tu respuesta (1-4): ")) #sigue preguntando
if ans == "1":
    g+=1
elif ans == "2":
    h+=1
elif ans == "3":
    r+=1
else:
    s+=1
print("Tienes que ir al bosque a rescatar a alguien, ¿qué haces?")
print("1.- llevas tu varita nada más")
print("2.- pides que algún amigo te acompañe")
print("3.- llevas pociones, y provisiones")
print("4.- decides involucrar a más gente que conozca el terreno, pero sin decirles a que vas")
ans = 0
while ans not in ["1","2","3","4"]: #mientras la respuesta no sea válida
    ans = str(input("Selecciona tu respuesta (1-4): ")) #sigue preguntando
if ans == "1":
    g+=1
elif ans == "2":
    h+=1
elif ans == "3":
    r+=1
else:
    s+=1
print("Tienes que tomar un libro, ¿Cuál eliges?")
print("1.- hechizos defensivos y ofensivos")
print("2.- hechizos de soporte y daño en área")
print("3.- alquimia avanzada")
print("4.- hechizos prohibidos")
ans = 0
while ans not in ["1","2","3","4"]: #mientras la respuesta no sea válida
    ans = str(input("Selecciona tu respuesta (1-4): ")) #sigue preguntando
if ans == "1":
    g+=1
elif ans == "2":
    h+=1
elif ans == "3":
    r+=1
else:
    s+=1
print("Te ofrecen ir a un viaje de gran desarrollo para tí únicamente, tú...")
print("1.- lo tomas pero después sientes remordimiento por tus amigos")
print("2.- decides no tomarlo, tus amigos son primero")
print("3.- tomas el viaje, pero buscas la manera de anotar lo que viste para compartirlo")
print("4.- lo tomas sin dudar")
ans = 0
while ans not in ["1","2","3","4"]: #mientras la respuesta no sea válida
    ans = str(input("Selecciona tu respuesta (1-4): ")) #sigue preguntando
if ans == "1":
    g+=1
elif ans == "2":
    h+=1
elif ans == "3":
    r+=1
else:
    s+=1
m = max(g,s,h,r) #tomamos el máximo
options = []
if g==m: #según cuales opciones alcanzaron el máximo se añaden unas casas u otras
    options.append("Griffindor")
if s==m:
    options.append("Slitterin")
if h==m:
    options.append("Humblepuff")
if r==m:
    options.append("Ravenclown")
#agregamos las opciones que más puntos tuvieron
if len(options)==1:
    print(f"No hay duda, mago, tu casa es {options[0]}")
else:
    print(f"Tengo dudas, mago, pero tus posibiles casas son {options}")