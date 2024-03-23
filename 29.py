"""
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 """
import re
def color_conversion(color_format: str) -> str:
    conversion = {"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"A"
                  ,"11":"B","12":"C","13":"D","14":"E","15":"F"}
    if type(color_format)==str and re.findall(r"\([0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\)",color_format)==[color_format]:
        #si se tienen tres números de a lo más tres cifras entre parentesis y separados por comas, es un rgb
        #if we have a a triplet of numbers with 1 to 3 digits between parenthesis and splited up by "," we have an rgb format
        color_format = color_format.replace("(","").replace(")","") #removemos ( y )
        r,g,b = color_format.split(",") #separamos en colores
        r,g,b = int(r),int(g),int(b) #los volvemos int
        if 0<=r<256 and 0<=g<256 and 0<=b<256:
            color = "#"
            for i in [r,g,b]:
                a = (i-(i%16)//16)%16
                b = i%16 #calculamos los digitos
                color+= conversion[str(a)]+conversion[str(b)] #añadimos los caracteres correspondientes
            return color
        else:
            print("el color no existe, recuerde tomar valores entre 0 y 255")
            return None
            
    elif type(color_format)==str and re.findall(r"#[A-F0-9]{6}",color_format)==[color_format]:
        #si se tiene un # seguido de 6 números del cero al 9, se trata de un hex largo
        #if we have the symbol # and six digits, we have a long hex
        first,second,third = color_format[1:3],color_format[3:5],color_format[5:], #separamos colores
        color = "("
        conversion = {v:k for k,v in conversion.items()} #invertimos la conversión
        for i in [first,second,third]:
            digit= int(conversion[i[0]])*16+int(conversion[i[1]]) #obtenemos el equivalente
            color+= str(digit)+","
        return color[:-1]+")" #agregamos el )            
    elif type(color_format)==str and re.findall(r"#[A-F0-9]{3}",color_format)==[color_format]:
        #finalmente si es un # con tres digitos se tiene un hex corto.
        #if we have # before three digits, we have a short hex
        first,second,third = color_format[1],color_format[2],color_format[3], #separamos colores
        color = "(" #inicializamos el valor
        conversion = {v:k for k,v in conversion.items()} #invertimos la conversión
        for i in [first,second,third]:
            digit= int(conversion[i[0]])*16 #obtenemos el equivalente
            color+= str(digit)+","
        return color[:-1]+")" #agregamos el )
    else:
        print("formato incorrecto, tu color debe tener alguno de los siguientes formatos: (r,g,b), #HEX, #HHEEXX")
        print("ejemplos: (180,0,233), #AAA, #F0C1D9")
        return None
rgb = "(255,0,0)"
hex_short = "#48F"
hex_long = "#33A7BC"
wrong_format_type = (123,123,22)
wrong_format_extra = "#4FCC"
wrong_format_extra_extra = "(12,12,34) pasd"
wrong_color_rgb = "(222,890,344)"
wrong_color_hex_s = "#GGG"
wrong_color_hex_l ="#ACACPW"
proofs = [rgb,hex_short,hex_long,wrong_format_type,wrong_format_extra,wrong_format_extra_extra,wrong_color_rgb,
          wrong_color_hex_s,wrong_color_hex_l]
print(list(map(color_conversion,proofs)))
