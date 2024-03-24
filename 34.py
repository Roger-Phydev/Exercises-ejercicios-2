""" 
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.
"""
"""
Previus: this is a complex problem, to solve it I used some theoric results like:
>Let v and w in R^2 vectors, so they're lineal dependents if and only if vxw=0 (x represents the cross product
but just taking the component z)
>note: v and w are lineal dependents by definition if and only if exist two numbers a,b (not both zero) such that
a*v + b*w = 0, when we have just two vectors, we just have to check that v=l*w or w=s*v with l or s in R.
Another way to see this is that v and w point to the same direction (or the opposite).
>>>>Solution:
To begin, we know that a particle will move according to: x(t) = x_0 + v_0*t where x is position, v velocity
and t is the time. So we have the next traces for the two particles:
x(t) = x_1 + v_1*t (particle1)
x(t) = x_2 + v_2*t (particle2)
there are solution just when we can find a t' that satisfy:
x_1 + v_1*t' = x_2 + v_2*t', and we can define the vectors Dx = x_2 - x_1 and Dv = v_2 - v_1.
So we're looking for a t' such that Dv*t' = - Dx, this impies that Dv and Dx are linear dependents, so  
Dx x Dv = 0 is the first condition.
But in order to solve the equation, the time must be positive, not null, neither negative. So, Dv and Dx must
be pointing in opposite directions, and that means that Dx.Dv < 0 where . means the scalar product.
So we find that the two particles collide if and only if Dx x Dv = 0 and Dx.Dv<0 note that because of
Dx.Dv<0 Dx and Dv must be not null.
If Dx=0 the two particles are the same, if Dv=0 and Dx!=0, they've got the same velocity but they're not
the same, so they're moving in parallel lines, so they're not going to collide.
Finally, it's easy to see that t' = |Dx|/|Dv|, where |*| represents the norm of the vector.
END

Este es un problema complejo, tuve que utilizar algunos resultados teóricos:
> Sean v,w vectores en R^2, entonces son linealmente dependientes si y solo si v x w = 0 donde x representa
el producto cruz, pero solo la componente z.
>nota: v y w son linealmente dependientes por definición si y solo si existen numeros a, b (no zero ambos)
tales que a*v + b*w = 0, con dos vectores esto equivale a v = l*w o w = s*v para l o s en R. Alternativamente
v y w apuntan en la misma dirección o en direcciones opuestas.
>>>>>>Solución:
Para empezar una particula se mueve con la siguiente relación: x(t) = x_0 + v_0*t con x la posición, v la 
velocidad y t el tiempo, asi que para las dos particulas tenemos:
x(t) = x_1 + v_1*t
x(t) = x_2 + v_2*t
Hay solución si podemos encontrar t' que cumpla que:
x_1 + v_1*t' = x_2 + v_2*t', además podemos definir los siguientes vectores Dx = x_2 - x_1 y Dv = v_2 - v_1.
Asi que buscamos t' tal que Dv*t' = -Dx, esto implica que Dv y Dx son linealmente dependientes, asi que 
Dx x Dv = 0 es la primer condición.
Pero para resolver la ecuación, el tiempo debe ser positivo, no nulo ni negativo. Así, Dv y Dx deben estar
apuntando en direcciones opuestas, y eso significa que Dx.Dv < 0, donde . es el producto escalar.
Asi que encontramos que dos particulas colisionan si y solo si Dx x Dv = 0 y Dx.Dv < 0 nota que debido a que
Dx.Dv <0 Dx y Dv deben ser no nulos.
Si Dx=0 las dos particulas son la misma, si Dv=0 y Dx!=0, tienen igual velocidad pero no son la misma, asi
que se están moviendo en lineas paralelas, asi que no colisionan.
Finalmente, es fácil ver que la solución es t' = |Dx|/|Dv| con |*| representando la norma del vector.
FIN
"""
def collide_time(x_1,v_1,x_2,v_2)->float:
    if {type(x_1),type(x_2),type(v_1),type(v_2)}.issubset({list,tuple}) and len(x_1)==len(x_2)==len(v_1)==len(v_2)>1:
        tipos = True #variable para saber si todos tienen el mismo tipo
        l = len(x_1)
        for i in range(l):
            tipos = tipos and {type(x_1[i]),type(x_2[i]),type(v_1[i]),type(v_2[i])}.issubset({int,float})
        #deben tener tipo tupla o list y deben tener longitud dos.
        if tipos:
            #deben tener tipo float o int en cada vector
            Dx = [x_2[j]-x_1[j] for j in range(l)] #definimos el vector diferencia
            if Dx == [0 for i in range(l)]:
                print("No hay colisión, inician en el mismo punto")
            else:
                Dv = [v_2[i]-v_1[i] for i in range(l)]
                if l in [2,3]:#en 2d y 3d
                    if l==2:#si es 2d lo volvemos 3D
                        Dx=[Dx[0],Dx[1],0]
                        Dv=[Dv[0],Dv[1],0]
                    #ahora definimos productos
                    point = Dx[0]*Dv[0]+Dx[1]*Dv[1]+Dx[2]*Dv[2]
                    cross = [Dx[1]*Dv[2]-Dx[2]*Dv[1],Dx[2]*Dv[0]-Dx[0]*Dv[2],Dx[0]*Dv[1]-Dx[1]*Dv[0]]
                    if Dv == [0,0,0]:
                        print("No hay colisión, se mueven en paralelo")
                    elif cross==[0,0,0] and point<0:
                        #si cumplen las condiciones
                        t = ((Dx[0]*Dx[0]+Dx[1]*Dx[1])/(Dv[0]*Dv[0]+Dv[1]*Dv[1]))**(0.5)
                        pos_1 = (x_1[0]+v_1[0]*t,x_1[1]+v_1[1]*t)
                        pos_2 = (x_2[0]+v_2[0]*t,x_2[1]+v_2[1]*t)
                        error = ((pos_1[0]-pos_2[0])**2 + (pos_2[1]-pos_1[1])**2)**0.5
                        print(f"Hubo colisión en {pos_1} a {t} segundo(s) con error {error}") #señalamos que hubo colisión
                        return t
                    else:
                        print("No hubo colisión")
                        return None
                else:
                    if Dv == [0 for i in range(l)]:
                        print("No hubo colisión, van en paralelo")
                        return None
                    sq_x = 0
                    sq_v = 0
                    for i in range(l):
                        sq_x+= Dx[i]*Dx[i]
                        sq_v+= Dv[i]*Dv[i]
                    time = (sq_x/sq_v)**(0.5)
                    pos_1 = [x_1[i]+time*v_1[i] for i in range(l)]
                    pos_2 = [x_2[i]+time*v_2[i] for i in range(l)]
                    error = 0
                    for i in range(l):
                        error+= (pos_2[i]-pos_1[i])**(0.5)
                    if error<0.001:
                        print(f"Hubo colisión con error {error} en {pos_1}")
                        return time
                    else:
                        print("no hubo colisión")
                        return None
        else:
            print("Error: tus entradas deben ser números enteros o flotantes")
            return None
    else:
        print("Error: debes usar vectores con tuplas o listas")
        print("Ejemplo: (0,0),[1,1],(1,0),[-1,1]")
        return None
a = [0]
print(a+[0])
collide_time((1,2),(1,1),"l",0) #wrong type
collide_time((1,2),[2,3,3],[2,2],(0,0)) #over-size
collide_time((0,0),[1,1],[0,0],[3,2]) #no collide same particle
collide_time((0,0),(0,1),(1,1),(0,1)) #no collide same velocity
collide_time((0,0),[1,1],(0,1),[1,-1]) # collission
collide_time((0,0),[0,2],(0,2),[0,-1]) #trivial collision
collide_time((0,0),[1,1],(1,1),[0.5,0.5]) #collision in line
collide_time((0,0),[-1,1],(-1,0),[3,0]) #no collide no trivial
print(collide_time((0,0),[2,3],(1,1),[0,1])) #collide no trivial
collide_time([1,0,0,0],[-1,1,0,0],[0,0,0,0],[0,1,0,0])