# Lista de ejercicios

## 01. Lenguaje hacker
### Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
* Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en "leet". (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

## 02. Partida de tenis
### Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado. El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien gane cada punto del juego. 
* Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
* Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
> 15 - Love
> 30 - Love
> 30 - 15
> 30 - 30
> 40 - 30
> Deuce
> Ventaja P1
> Ha ganado el P1
* Si quieres, puedes controlar errores en la entrada de datos.
* Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   

## 03.Generador de contraseñas
### Escribe un programa que sea capaz de generar contraseñas de forma aleatoria. Podrás configurar generar contraseñas con los siguientes parámetros:
* Longitud: Entre 8 y 16.
* Con o sin letras mayúsculas.
* Con o sin números.
* Con o sin símbolos.
### Pudiendo combinar todos estos parámetros entre ellos.

## 04. Fibonacci primo par
### Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par. Ejemplos:
* Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
* Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

## 05. Hola mundo
### Escribe un !Hola Mundo! en todos los lenguajes de programación que puedas. Seguro que hay algún lenguaje que te llama la atención y nunca has utilizado, o quizás quieres dar tus primeros pasos... ¡Pues este es el momento! A ver quién se atreve con uno de esos lenguajes que no solemos ver por ahí...

## 06. Piedra, papel, tijeras, lagarto, spok
### Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
* El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
* La función recibe un listado que contiene pares, representando cada jugada.
* El par puede contener combinaciones de "🗿" (piedra), "📄" (papel), "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
* Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
* Debes buscar información sobre cómo se juega con estas 5 posibilidades.

## 07. Sombrero seleccionador
### Crea un programa que simule el comportamiento del sombrero selccionador del universo mágico de Harry Potter.
* De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
* Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
* En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que coloque al alumno en una de las 4 casas de Hogwarts: (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
* Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador:Por ejemplo, en Slytherin se premia la ambición y la astucia.

## 08. Generador pseudo aleatorio
### Crea un generador de números pseudoaleatorios entre 0 y 100.
* No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
* Es más complicado de lo que parece...

## 09. Heterograma, paragrama, pangrama
### Crea 3 funciones, cada una encargada de detectar si una cadena de texto es un heterograma, un isograma o un pangrama.
* Debes buscar la definición de cada uno de estos términos.

## 10. Parámetros url
### Dada una URL con parámetros, crea una función que obtenga sus valores. No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
* Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0 los parámetros serían ["2023", "0"]

## 11. Viernes trece
### Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
* La función recibirá el mes y el año y retornará verdadero o falso.

## 12. Adivina la palabra
### Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
* El juego comienza proponiendo una palabra aleatoria incompleta. Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
* El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que la palabra a adivinar)
* Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta    uno al número de intentos
* Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno al número de intentos
* Si el contador de intentos llega a 0, el jugador pierde
* La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
* Puedes utilizar las palabras que quieras y el número de intentos que consideres

## 13. Octal y hexadecimal
### Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal.
* No está permitido usar funciones propias del lenguaje de programación que realicen esas operaciones directamente.

## 14. Aurebesh
### Crea una función que sea capaz de transformar Español al lenguaje básico del universo Star Wars: el "Aurebesh".
* Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
* También tiene que ser capaz de traducir en sentido contrario.

## 15. Juego de piedra, papel y tijeras
### En este reto debes contruir un programa que permita jugar piedra papel o tijeras en un 2 de 3.

## 16. Análisis de textos
### Crea un programa que analice texto y obtenga:
* Número total de palabras.
* Longitud media de las palabras.
* Número de oraciones del texto (cada vez que aparecen un punto).
* Encuentre la palabra más larga.
### Todo esto utilizando un único bucle.

## 17. La trifuerza
### ¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! Crea un programa que dibuje una Trifuerza de "Zelda" formada por asteriscos.
* Debes indicarle el número de filas de los triángulos con un entero positivo (n).
* Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
### Ejemplo: Trifuerza 2
>###  \*
>###   \*\*\*
>###     \*   \*
>### \*\*\* \*\*\*

## 18. Primos gemelos
### Crea un programa que encuentre y muestre todos los pares de números primos gemelos en un rango concreto. El programa recibirá el rango máximo como número entero positivo. 
* Un par de números primos se considera gemelo si la diferencia entre ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
* Ejemplo: Rango 14 (3, 5), (5, 7), (11, 13)

## 19. La espiral
### Crea una función que dibuje una espiral como la del ejemplo.
* Únicamente se indica de forma dinámica el tamaño del lado.
* Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
* Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝

## 20. Cifrado césar
### Crea un programa que realize el cifrado César de un texto y lo imprima. También debe ser capaz de descifrarlo cuando así se lo indiquemos.
* Te recomiendo que busques información para conocer en profundidad cómo realizar el cifrado. Esto también forma parte del reto.

## 21. Código konami
### Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.

## 22. Cuenta atrás
### Crea una función que reciba dos parámetros para crear una cuenta atrás. 
* El primero, representa el número en el que comienza la cuenta.
* El segundo, los segundos que tienen que transcurrir entre cada cuenta. Sólo se aceptan números enteros positivos.
* El programa finaliza al llegar a cero.
* Debes imprimir cada número de la cuenta atrás.

## 23. Expresiones matemáticas
### Crea una función que reciba una expresión matemática (String) y compruebe si es correcta. Retornará true o false.
* Para que una expresión matemática sea correcta debe poseer un número, una operación y otro número separados por espacios.
* Tantos números y operaciones como queramos.
* Números positivos, negativos, enteros o decimales.
* Operaciones soportadas: + - * / %
### Ejemplos:
* "5 + 6 / 7 - 4" -> true
* "5 a 6" -> false

## 24. Caracter infiltrado
### Crea una función que reciba dos cadenas de texto casi iguales, a excepción de uno o varios caracteres. La función debe encontrarlos y retornarlos en formato lista/array.
* Ambas cadenas de texto deben ser iguales en longitud.
* Las cadenas de texto son iguales elemento a elemento.
* No se pueden utilizar operaciones propias del lenguaje que lo resuelvan directamente.
### Ejemplos:
* Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
* Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]

## 25. Teclado T9
### Los primeros dispositivos móviles tenían un teclado llamado T9 con el que se podía escribir texto utilizando únicamente su teclado numérico (del 0 al 9). Crea una función que transforme las pulsaciones del T9 a su representación con letras.
* Debes buscar cuál era su correspondencia original.
* Cada bloque de pulsaciones va separado por un guión.
* Si un bloque tiene más de un número, debe ser siempre el mismo.
* Ejemplo: Entrada-> 6-666-88-777-33-3-33-888  Salida-> MOUREDEV

## 26. Ábaco
### Crea una función que sea capaz de leer el número representado por el ábaco.
* El ábaco se representa por un array con 7 elementos.
* Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar   operaciones) para las cuentas y una secuencia de "---" para el alambre.
* El primer elemento del array representa los millones, y el último las unidades.
* El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
### Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 
## 27. Columnas de Excel
### Crea una función que calcule el número de la columna de una hoja de Excel teniendo en cuenta su nombre.
* Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
* Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.

## 28. Permutaciones
### Crea un programa que sea capaz de generar e imprimir todas las permutaciones disponibles formadas por las letras de una palabra.
* Las palabras generadas no tienen por qué existir.
* Deben usarse todas las letras en cada permutación.
* Ejemplo: sol, slo, ols, osl, los, lso 

## 29. Colores hex y rgb
### Crea las funciones capaces de transformar colores HEX a RGB y viceversa.
### Ejemplos:
* RGB a HEX: r: 0, g: 0, b: 0 -> #000000
* HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
* Si no existen combinaciones, retornar una lista vacía

## 30. Sumas
### Crea una función que encuentre todas las combinaciones de los números de una lista que suman el valor objetivo.
* La función recibirá una lista de números enteros positivos y un valor objetivo.
* Para obtener las combinaciones sólo se puede usar una vez cada elemento de la lista (pero pueden existir elementos repetidos en ella).
* Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6 Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
* Si no existen combinaciones, retornar una lista vacía

## 31. Triples pitagóricos
### Crea una función que encuentre todos los triples pitagóricos (ternas) menores o iguales a un número dado.
* Debes buscar información sobre qué es un triple pitagórico.
* La función únicamente recibe el número máximo que puede aparecer en el triple.
* Ejemplo: Los triples menores o iguales a 10 están formados por (3, 4, 5) y (6, 8, 10).

## 32. Tabla de multiplicar
### Crea un programa que sea capaz de solicitarte un número y se encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
* Debe visualizarse qué operación se realiza y su resultado.
* Ej: 
*     1 x 1 = 1
*     1 x 2 = 2
*     1 x 3 = 3
*     ... 

## 33. La casa encantada
### Este es un reto especial por Halloween. Te encuentras explorando una mansión abandonada llena de habitaciones. En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente. Tu misión es encontrar la habitación de los dulces.
* Se trata de implementar un juego interactivo de preguntas y respuestas por terminal. (Tienes total libertad para ser creativo con los textos)
* 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4 que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma. (16 habitaciones, siendo una de entrada y otra donde están los dulces)
* Esta podría ser una representación:
*   🚪⬜️⬜️⬜️
*   ⬜️👻⬜️⬜️
*   ⬜️⬜️⬜️👻
*   ⬜️⬜️🍭⬜️
* ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto. Si no lo aciertas no podrás desplazarte.
* 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
* 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
* 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y tengas que responder dos preguntas para salir de ella.

## 34. Punto de encuentro
### Crea una función que calcule el punto de encuentro de dos objetos en movimiento en dos dimensiones.
* Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento (vector de desplazamiento) por unidad de tiempo (también en formato xy).
* La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
* La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardaron en lograrlo.
* La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.

## 35. Simulador de clima
### Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia) de un lugar ficticio al pasar un número concreto de días según estas reglas:
* La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
### Cada día que pasa:
* 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
* Si la temperatura supera los 25 grados, la probabilidad de lluvia al día siguiente aumenta en un 20%.
* Si la temperatura baja de 5 grados, la probabilidad de lluvia al día siguiente disminuye en un 20%.
* Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
* La función recibe el número de días de la predicción y muestra la temperatura y si llueve durante todos esos días.
* También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.