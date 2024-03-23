from datetime import date
def is_there_friday_the_thirteen(year,month):
    if date(year,month,13).weekday()==4: #si el día de la semana correspondiente al 13 del mes y año introducidos
        return True #regresa verdadero
    else:
        return False #en caso contrario da falso
print(is_there_friday_the_thirteen(2023,1)) #en enero de 2023 si hubo un viernes trece
print(is_there_friday_the_thirteen(1996,5)) #en el mes que nací del no hubo
a = "spldre"