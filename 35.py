""" 
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
"""
from random import randint as rd
def weather_sim(num_of_days:int,init_temp:float,rain_prob:float)->dict:
    if type(num_of_days)==int and num_of_days>1:
        if (type(init_temp)==int or type(init_temp)==float) and init_temp>-273.15:
            if (type(rain_prob)==int or type(rain_prob)==float) and rain_prob>=0 and rain_prob<=100:
                temp = init_temp
                prob = rain_prob
                weather_report = dict() # creamos el dict que devolvemos
                weather_report['Temperatura máxima'] = init_temp
                weather_report['Temperatura mínima'] = init_temp
                weather_report['Días con lluvia'] = 0
                weather_report['datos'] = [[init_temp,rain_prob]]
                next_day = [0,0] #sirve para saber que aplicaremos al día siguiente
                if init_temp>25:
                    next_day[1]=20
                elif init_temp<5:
                    next_day[1]=-20
                if rain_prob==100:
                    weather_report['Días con lluvia']+=1
                    next_day[0]=-1
                for i in range(num_of_days-1):#recorremos los días
                    p = rd(1,1000)#elegimos un aleatorio entre 1 y 1000
                    if p<=100: #si es menor o igual a 100 (10% de prob)
                        temp+=2
                    elif p<=200: #como no se cumplió lo ant, p>100, asi que es otro 10%
                        temp-=2
                    temp+=next_day[0]#añadimos lo correspondiente al dia anterior
                    prob+=next_day[1]
                    if prob>=100: prob = 100 #vemos que no pase de 100
                    weather_report['datos'].append([temp,prob]) #agregamos el dato
                    weather_report['Temperatura máxima']=max(weather_report['Temperatura máxima'],temp)
                    weather_report['Temperatura mínima']=min(weather_report['Temperatura mínima'],temp)
                    if prob ==100:
                        weather_report['Días con lluvia']+=1
                        next_day[0]=-1
                    else:
                        next_day[0]=0
                    if temp>25:
                        next_day[1]=20
                    elif temp<5:
                        next_day[1]=-20
                    else:
                        next_day[1]=0
                print(f'T_max : {weather_report["Temperatura máxima"]} , T_min : {weather_report["Temperatura mínima"]}, días con lluvia : {weather_report["Días con lluvia"]}')
                return weather_report
            else:
                print("Error, la probabilidad de lluvia es un número entre 0 y 100")
        else:
            print("Error, la temperatura debe ser un número mayor a -273.15, en °C")
    else:
        print("Error, la cantidad de días debe ser 2,3... etc.")
print(weather_sim(7,24,90)["datos"])
