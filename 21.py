from pynput import keyboard as kb #importamos la libreria necesaria 
konami_code = "Key.upKey.upKey.downKey.downKey.leftKey.rightKey.leftKey.right'b''a'Key.enter" #ponemos el codigo konami
point = ""
def ipt(tecla): #creamos una función para la pulsación
    global point #importamos la variable
    if str(tecla) == "Key.esc":#con esto hacemos que se pare
        return False
    point+=str(tecla) #sumamos la tecla introducida
def rls(tecla): #creamos otra función para el rechazo
    global point #importamos la variable global
    print (point)
    if point.find(konami_code)!=-1: #si encuentra el codigo konami entre la cadena
        print(f"En efecto, lograste el código konami: {konami_code}")
        return False #y salimos
print("¿Conoces el código Konami? Intenta meterlo.(Enter==Start) \nnota: Si quieres salir,teclea esc")
kb.Listener(ipt,rls).run()
