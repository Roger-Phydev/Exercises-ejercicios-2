# Information list

## 01. Hacker language
### Write a program that receives a text and transform natural language into "Hacker language" (know as "leet" or "1337" as well). This language replaces alphanumeric characters.
* Use the table:(https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) and take into account just the firs option. Example: "4" == "a"

## 02. Tennis game
### Write a program that shows how a tennis game evolves and who has won. The program will receive a sequence of expresions "P1" (Player 1) or "P2" (Player 2), according to who wins each point.
* The possible expressions are "Love" (zero), 15, 30, 40, "Deuce" (Tie), "Advantage" .
* If the program receives [P1, P1, P2, P2, P1, P2, P1, P1], it'll show:
> 15 - Love
> 30 - Love
> 30 - 15
> 30 - 30
> 40 - 30
> Deuce
> Advantage P1
> P1 wins
* If you want, you can control errors in the parameters.
* Check the rules if you don't understand how it works.

## 03. Password generator
### Write a program that is able to generate passwords in a random way. You can configure the password generation using the next parameters:
* Lenght: Between 8 y 16.
* Upper case or not
* Numbers or not
* Special symbols or not
### You can combine all the parameters, for example: "sdr6/?=t" (has 8 symbols, uses numbers, special symbols but not upper case).

## 04. Fibonacci prime even
### Write a program that, given a number, checks and shows if the number is prime, fibonacci and even. Examples:
* For 2 it'll show: "2 is prime, fibonacci and even"
* For 7 it'll show: "7 is prime, is not fibonacci and is odd"

## 05. Hello world
### Write Hello World! in all languages you can. This is a good starting pointo to learn some new language, do it.

## 06. Rock, paper, scissors, lizard, spok
### Make a program that calculates who wins the most rounds of rock, paper, scissors, lizard, spock.
* The result might be: "Player 1", "Player 2", "Tie".
* The function receives a list that cointains pairs which represent a round.
* The pair must contain combinations of "🗿" (rock), "📄" (paper), "✂️" (scissors), "🦎" (lizard) or "🖖" (spock).
* Example-> Input: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Result: "Player 2".
* You must find information about how to play this style of game.

## 07. Sorting hat
### Make a program which simulates the behavior of the sorting hat (from the magic universe of Harry Potter).
* If it's possible it'll ask 5 questions (at least) via the terminal.
* Every question will have 4 possible answers (and it receives the answer via the terminal).
* Depending on the answers, you must design an algorithm that selects a school house for the student: (Gryffindor, Slytherin , Hufflepuff or Ravenclaw)
* You must take into account the features of every house to make the questions and answers: Example, Slytherin rewards ambition and cunning.

## 08. Pseudo-aleatory generator
### Make a pseudo-aleatory number generator between 0 and 100.
* You mustn't use any "random" function (or something like that)
* It's more complicated that it seems...

## 09. Heterogram, isogram, pangram
### Make 3 functions, each of them detects whether a string is an heterogram, isogram or pangram (repectivitely) or not.
* You must find the definition of every term.

## 10. Url parameters
### Given an url with parameters, make a function that obtains its values. You can't use operations that perform this task directely.
* Example: In the url https://retosdeprogramacion.com?year=2023&challenge=0 its parameters are ["2023", "0"]

## 11. Friday the thirteenth
### Make a function able to detect whether there is a Friday thirteenth in the month and year selected by the user.
* The function will receive the month and year and return True or False.

## 12. Guess the word
### Make a little game about guessing a word with a max number of attempts:
* The game will begin showing a random uncompleted word. For example "m_s__ry", and the number of tries left.
* The user can introduce only a single letter o a word (with exactly the same length that the word to be guessed).
* If the user writes a letter and it is right, it shows that letter in the word. If the user fails, it reduces the number of attempts by one.
* If the user writes the word correctely, it ends, otherwise the number of attempts is reduced by one.
* If the attempts counter reaches 0, the player loses.
* The word must hide letters randomly, and must never hide more than 60% of the word.
* You can use as many words and attempts as you want.

## 13. Octal and hexadecimal
### Make a function that receives a number (decimal) and turns into an octal and hexadecimal number.
* Functions that simplify the problem mustn't be used.

## 14. Aurebesh
### Make a function able to transform English into the basic language in the Star wars universe: "Aurebesh".
* Symbols that doesn't exist in "Aurebesh" can be avoided.
* It has to be able to translate in the other direction (Aurebesh->English).

## 15. Rock, paper, scissors: the game
### You must make a program that allows you to play rock, paper, scissors for three rounds (if you win/lose two rounds, you win/lose the game).

## 16. Text analysis
### Make a program that analyzes a text and obtains:
* Total number of words
* Average word lenght
* Number of sentences in the text (each time a period appears).
* Find the longest word
### Using only one loop (for/while).

## 17. Triforce
### Make a program that draws a triforce (from Zelda) made of "*".
* You must indicate the number of rows of the triangles with a positive integer number(n).
* Each triangle will calculates its longest row using the formula: 2n-1.
### Example: Triforce 2
>###  \*
>###   \*\*\*
>###     \*   \*
>### \*\*\* \*\*\*

## 18. Twin primes
### Make a program that finds and displays all pairs of twin primes numbers whitin a given range. The program will receive the maximum range as a positive integer number.
* A pair of primes are twin primes if the difference between them is exactely two. For example: (3,5) or (11,13).
* Example: Range 14 -> (3, 5), (5, 7), (11, 13)

## 19. Spiral
### Make a function that draws a spiral
* You only have to indicate the size of the side.
* Allowed symbols: ═ ║ ╗ ╔ ╝ ╚
* Example: 5-sided spiral (5 rows and 5 columns):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝

## 20. Caesar cipher
### Make a program that performs a Caesar cipher of a text and displays it. It is also capable of deciphering it if we tell it to.
* Find information about it.

## 21. Konami code
### Make a program that detects the famous "Konami Code" if it has been written correctly. If it happens, the program should display a message in the terminal.

## 22. Countdown
### Make a function that takes two parameters to create a countdown. 
* The first parameter, represents the number at which the countdown begins.
* The second one, the seconds that the countdown lasts. Only positive integer numbers are allowed.
* The program ends when it reaches zero.
* You must print each number of the countdown.

## 23. Math expressions
### Make a function that takes a math expression(String) and checks if its correct. It'll return True or False.
* A correct math expression has to be a number, an operation and another number divided by a space.
* As many numbers and operations as we want.
* Accepts positive, negative, integers and decimal numbers.
* Operations supported: + - * / %
### Examples:
* "5 + 6 / 7 - 4" -> true
* "5 a 6" -> false

## 24. Infiltrated symbols
### Make a function which takes two strings almost identical, with the exception of one or more symbols. It must find them and return them in a list.
* Both strings must to be the same lenght.
* Operations that solve the problem directly cannot be used
### Example:
* My name is Roger / My neme is Rogor -> ["e", "o"]
* My name is.Roger Parra / My name is roger parra -> [" ", "r", "p"]

## 25. T9 keyboard
### Many years ago, cellphones had a special kind of keyboard, the so called "T9 keyboard". It could be used to write text only using numbers (0-9). Make a function that transforms T9 keystrokes into letters.
* You have to find what is the original correspondence.
* Each block of keystrokes is separated by a "-".
* If a block has more than one number, it must be the same.
* Example: Input-> 777-666-4-33-777 output-> ROGER

## 26. Abacus
### Make a function capable of reading the number represented by an abacus.
* The abacus is represented by a list of seven elements.
* Each elemente will have 9 "O" (it is also usual it has 10 in order to do operations) to the beads and a sequence "---" to represent the wire.
* The fist element in the list represents "millions" and the last one, represents units.
* The number at each element is represented by the beads on the left side of the wire.
### Example of list and result:
* ["O---OOOOOOOO",
*  "OOO---OOOOOO",
*  "---OOOOOOOOO",
*  "OO---OOOOOOO",
*  "OOOOOOO---OO",
*  "OOOOOOOOO---",
*  "---OOOOOOOOO"]
*  Result: 1,302,790
 
## 27. Excel columns
### Make a function that calculates the number of columns on an Excel sheet using its name. 
* The columns are labeled using letters from "A" to "Z" infinitely. 
* Examples: A = 1, Z = 26, AA = 27, CA = 79.

## 28. Permutations
### Make a program capable of generating and printing all permutations formed of the letters of a word.
* The generated words don't have to make sense (semantically).
* All letters in the word must be used in each permutation.
* Example: sun, snu, uns, usn, nus, nsu. 

## 29. Hex and rgb colors
### Make the functions capables of transforming hex colors to rgb and vice versa.
### Examples:
* RGB to HEX: r: 0, g: 0, b: 0 -> #000000
* HEX to RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
* If there are no joins, returns an empty list.

## 30. Sums
### Make a function that finds all the number combinations from a list that sums a target value.
* The function takes a list of positive integer numbers and a target value.
* To obtain the combinations, only an element can be used at a time (but the list may contain repeated numbers).
* Example: List = [1, 5, 3, 2], Target = 6 Solutions: [1, 5] and [1, 3, 2] (both of them sums 6)
* If there are no solutions, returns an empty list.

## 31. Pythagorean triple
### Crate a function that finds all Pythagorean triples less than or equal to a given number.
* You must find some informations about Pythogorean triples.
* The functions only takes the maximum number that can appear in the triple.
* Example: The triples less than or equal to 10 are (3, 4, 5) and (6, 8, 10).

## 32. Multiplication tables
### Create a program capable of asking for a number and printing its multiplication table between 1 and 10.
* Must display what the operation is in use and its result.
* Ex:
* 1 x 1 = 1
* 1 x 2 = 2
* 1 x 3 = 3
*...

## 33. Haunted house
### You're exploring an abandoned mansion full of rooms. In each rom you will have to solve a riddle to move on to the next one. Your mission: find the candy room.
* You have to create an interactive question and answer game through the terminal. (You're free to create your own texts)
* 🏰 Mansion: Corresponds to a 4x4  square structure that you must simulate. The door room and candy room have no riddle. (16 rooms, one for the entrance and another where the candies are)
* This might be a representation:
*   🚪⬜️⬜️⬜️
*   ⬜️👻⬜️⬜️
*   ⬜️⬜️⬜️👻
*   ⬜️⬜️🍭⬜️
* ❓ Riddles: Each normal room have a random riddle that you must answer with text. If you make a mistake, you will not be able to move.
* 🧭 Move: If you solve the riddle, you will select where you want to move (Example: north/south/east/west. It only accepts one of these possible options)
* 🍭 Exit: You leave the mansion when you find the candy room.
* 👻 (Bonus) Ghosts: there is a 10% chance that a ghost  will appear in a room and you will have to answer two riddles to leave the room.

## 34. Meeting point
### Create a function that finds the meeting point of two objects moving in two dimensions.
* Each object is composed of a coordinate (x,y) and a velocity vector.
* The function takes the origin coordinates of both objects and their velocities
* Calculates and shows the point at they meet and the time it took to get there.
* It must be taken into account that the objects may not meet

## 35. Weather simulator
### Create a function that simulates the weather conditions (temperature, rain probability) of a fictitious location after a given number of days according to the following rules:
* Initial temperature and probability of rain are defined by the user
### Each day:
* 10% chance that the temperature will rise or fall 2 degrees.
* If the temperature exceeds 25 degrees, the probability of rain will increase by  20% the next day.
* If the temperature is below 5 degrees, the probability of rain will decrease by 20% the next day.
* If it rains (100%), the temperature will drop 1 degree the next day.
* The function takes the number of days and shows the temperature and rain conditions every day.
* It also shows the maximum and minumum temperature during the period and how many days it will rain.