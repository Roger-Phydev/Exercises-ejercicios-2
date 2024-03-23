#usaremos expresiones regulares, para ello nos damos cuenta que los parámetros vienen de la siguiente manera:
# www.saoi.... .com?variable=parametro&valor=parametro&...
#en conclusión, lo que buscamos está entre un signo = y, un & o es el final de la cadena
import re
def parameters_url(url):
    if type(url)==str:
        parameter = r"(?<=)[\w]+(?=&|$)" #nuestra expresión regular es simple:
        #debe haber antes un símbolo igual, luego una o más caracteres de palabras y debe haber después un & o es el final de la cadena
        return re.findall(parameter,url) #devolvemos la lista de coincidencias
print(parameters_url("https://retosdeprogramacion.com?year=2023&challenge=0")) #funciona con el ejemplo

