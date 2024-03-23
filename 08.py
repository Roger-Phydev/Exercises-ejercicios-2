import datetime
def rand_gen_100():
    s = datetime.datetime(1,1,1).today() #creamos esta semilla
    s = s.microsecond
    return s%101 #devolvemos lo que quema en 101 dando nuestro número aleatorio
print(rand_gen_100())
s = 0
for i in range(10000):
    s+= rand_gen_100()/10000
print(s)