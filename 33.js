"use strict";
////////////////////////////////////////////////////////////
/* Important: this file needs to work the next files: 
hauntedhouse.html
hauntedhouse.css
images
But all of these files you'll find at my repository "Retos_Python_2"
*/
////////////////////////////////////////////////////////////
///////
// generate random
const randGen = k=>{
    return Math.round(k*Math.random()-0.5);
};
//////
// questions
const questions = [
    ['En la saga zelda ¿Cuál juego de zelda salió en el año 2000?','ocarina of time','majoras mask','minish cap','wind waker','B'],
    ['¿En que juego de zelda apareció Ganondorf por primera vez?','zelda 1','a link to the past','wind waker','ocarina of time','D'],
    ['En breath of the wild de la saga zelda, existen muchas semillas kolog, ¿cuántas aproximadamente?','entre 100 y 150','entre 300 y 600','entre 800 y 900','más de 1000','C'],
    ['¿Cuál es la espada más simbólica de la saga the legend of zelda?','espada maestra','biggoron','espada kokiri','espada del guardián','A'],
    ['En la saga zelda ¿Las bombas sirven, aparte de como armas arrojadizas, para...?','abrir portales','conseguir armas','abrir zonas ocultas','invocar una deidad','C'],
    ['En la saga halo, ¿Cómo se llaman los villanos de la trilogía original?','covenant','final killers','troops','erasers','A'],
    ['En halo 4 ¿Cuáles de estos enemigos hacen su aparición por primera vez?','grunts','elites','hunters','knights','D'],
    ['En la saga halo, ¿Qué es un halo?','un enemigo','el jefe final','un arma muy poderosa','el protagonista','C'],
    ['En la saga halo, Arma icónica de la saga que no aparece en halo 2:','rifle de batalla','rifle de asalto','spnkr','rifle de plasma','B'],
    ['Cuando completas este juego de la saga halo NO aparece una escena especial','halo 2','halo 3','halo CE','halo infinite','A'],
    ['En la saga gears hay un personaje muy importante que se sacrifica en gears 3, ¿Quién es?','Dominic Santiago','Tai','Marcus Phoenix','August Cole','A'],
    ['El arma emblema de la saga gears of war tiene acoplada una...','lanza','espada','trituradora','motosierra','D'],
    ['En la saga gears of war hay un arma muy poderosa que solo se puede usar al aire libre con ayuda de satélites,¿Cuál es?','lancer','gnasher','martillo del alba','dropshot','C'],
    ['Durante gears 5, hay dos partes abiertas, ¿En qué biomas se basan?','selva y bosque','ninguno, son ciudades','estepa y desierto','bosque y montaña','C'],
    ['Nombre del enemigo principal en la saga gears of war','locust/larvas','alianza','federación','razors','A'],
    ['En los juegos de Mario, es el item principal:','champiñón','estrella','caparazón','hoja','A'],
    ['¿Cuál juego de mario se ambienta en el espacio?','Super mario 3','Super mario Space','Super mario galaxy','Super mario sunshine','C'],
    ['¿Cómo se llama el hermano de mario?','Luis','Luigi','Leandro','Lino','B'],
    ['En super mario 3, ¿Cuál item aparece menos?','estrella','champiñón','traje de tanuki','flor de fuego','C'],
    ['En super mario world, ¿Qué personaje comparte el protagonismo con Mario?','Toad','Luigi','Bowser','Yoshi','D'],
    ['Assasins Creed 2 se lleva a cabo en...','Italia','Francia','Egipto','Arabia','A'],
    ['Este título de Assasins creed se ambienta en la independencia de Estados Unidos:','Assasins creed 3','Assasins creed Origins','Assasins creed IV','Assasins creed Unity','A'],
    ['Arma emblema de la saga Assasins creed','hacha doble','hoja oculta','bastón','arco','B'],
    ['En la saga Assasins creed se usa mucho este deporte urbano','Parkour','Skate','BMX','Esgrima','A'],
    ['En la saga Assasins creed son los enemigos principales','Unión de bandidos','Orden de asesinos','Templarios','Tropas del miedo','C'],
    ['Juego de call of duty que toca la guerra de Vietnam','modern warfare','world at war','black ops','advanced warfare','C'],
    ['En minecraft, ¿cuál arma es la más emblemática?','Arco','Espada','Pico','Lanza','C'],
    ['En la saga Kirby, ¿Qué item te vuelve invencible momentaneamente?','paleta de caramelo','estrella','nuez','jugo de naranja','A'],
    ['En hi-fi rush, importa tener buen...','tino','ritmo','arma','tiempo','B'],
    ['¿Cuál juego de los siguientes NO es de rol?','Final Fantasy','Dragon quest','Starfield','Grim fandango','D']
];
let long = questions.length;
let selectQ;
////////
// elements needed
const house = [
    document.querySelectorAll(".row-1"),
    document.querySelectorAll(".row-2"),
    document.querySelectorAll(".row-3"),
    document.querySelectorAll(".row-4")
];
const info = document.getElementById("info");
const moves = document.querySelectorAll(".dir");
const question = document.getElementById("q");
const options = document.querySelectorAll(".op");
const answer = document.getElementById("ans");
const reload = document.getElementById("reload");
const images = [
    "images/ghost.jpg",
    "images/monster.jpg",
    "images/question.jpg",
    "images/door.jpg",
    "images/candies.jpg"
];
let attempts = 5;
let numQuestions = 0;
const scrollConfig = {
    behavior: 'smooth',
    block: 'start',
};
///////
// generating map
let houseG = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
houseG = houseG.map(val=>val.map(item=>{
    let s = randGen(10)
    if(s==0){
        return images[0];
    }else{
        return images[1];
    }
}));
let cursor = [0,0]; //siempre inicia en 0,0
let a = randGen(4),b=randGen(4);
while(a<2||b<2){
    a = randGen(4);
    b = randGen(4);
}
houseG[0][0] = images[3];
houseG[a][b] = images[4];
////////
//painting house
house.forEach((row,i) => {
    row.forEach((column,j)=>{
        if(i==0&&j==0){
            column.setAttribute("src",images[3]);
        }else{
            column.setAttribute("src",images[2]);
        }
    })
});
house[cursor[0]][cursor[1]].classList.toggle("actual");
/////////
//move actions
let enabled = [false,false,true,true]; // this let move or not in a direction
const checkEnable = position=>{ //checks which directions are available
    if(position[0]==0){
        enabled[0] = false;
        enabled[3] = true;
    }else if(position[0]==3){
        enabled[0] = true;
        enabled[3] = false;
    }else{
        enabled[0] = true;
        enabled[3] = true;
    }
    if(position[1]==0){
        enabled[1] = false;
        enabled[2] = true;
    }else if(position[1]==3){
        enabled[1] = true;
        enabled[2] = false;
    }else{
        enabled[1] = true;
        enabled[2] = true;
    }
}
////////
// move events.
moves.forEach((direction,i)=>{
    direction.addEventListener("click",()=>{
        if(enabled[i]){//it only works if the direction is available
            let dir = [[0,-1],[1,-1],[1,1],[0,1]];
            house[cursor[0]][cursor[1]].classList.toggle("actual");
            cursor[dir[i][0]]+=dir[i][1];//changes the cursor
            let a = cursor[0],b=cursor[1];
            house[a][b].classList.toggle("actual");//change the images and style
            if(house[a][b].getAttribute("src")=="images/ok.jpg"||
            house[a][b].getAttribute("src")=="images/door.jpg"){
                info.innerText = "Ya pasaste por aquí, elige otra dirección";
            }else{
                house[a][b].setAttribute("src",houseG[a][b]);
            }
            if(house[a][b].getAttribute("src")=="images/monster.jpg"){
                info.innerText= `Tendras que responder para continuar.\n vidas: ${attempts}`;
                moves[0].parentElement.style = "display:none;";
                question.parentElement.style = "display:block;";
                selectQ = randGen(long);
                question.innerText = questions[selectQ][0]+"\n";
                question.innerText+= `A) ${questions[selectQ][1]} 
                B) ${questions[selectQ][2]}\n C) ${questions[selectQ][3]}
                D) ${questions[selectQ][4]}`;
                numQuestions = 1;
            }else if(house[a][b].getAttribute("src")=="images/ghost.jpg"){
                info.innerText= `Oh no, tendrás que responder dos preguntas.\n vidas: ${attempts}`;
                moves[0].parentElement.style = "display:none;";
                question.parentElement.style = "display:block;";
                selectQ = randGen(long);
                question.innerText = questions[selectQ][0]+"\n";
                question.innerText+= `A) ${questions[selectQ][1]} 
                B) ${questions[selectQ][2]}\n C) ${questions[selectQ][3]}
                D) ${questions[selectQ][4]}`;
                numQuestions = 2;
            }else if(house[a][b].getAttribute("src")=="images/candies.jpg"){
                info.innerText="Ganaste, llegaste a los dulces";
                moves[0].parentElement.style = "display: none;";
                question.parentElement.style = "display: none;"               
                reload.style = "display: inline;"
            }
            house[cursor[0]][cursor[1]].scrollIntoView(scrollConfig);
            checkEnable(cursor); //check directions

        }
    })
})
///////
// question events:
answer.addEventListener("click",()=>{
    let ans = answer.previousElementSibling.value; //read value
    let another = numQuestions==2; //if there were 2 q
    if(ans==questions[selectQ][5]){
        numQuestions--;//decreses the number of questions
    }else{
        attempts--;//decreases attempts
        info.innerText = `Mal, vuelve a intentarlo\n vidas: ${attempts}`;
    }
    if(attempts==0){//if there is no remaining attempts, you loose
        info.innerText = "Lo siento, te quedaste sin vidas\n HAS PERDIDO";
        moves[0].parentElement.style = "display:none;";
        question.parentElement.style = "display: none;";
        reload.style = "display: inline;";
    }
    if(numQuestions==0){//if there is no questions remaining, go to move
        info.innerText = "Bien, superado... avanza";
        moves[0].parentElement.style = "display: grid;";
        question.parentElement.style = "display: none;";
        info.scrollIntoView(scrollConfig);
        house[cursor[0]][cursor[1]].setAttribute("src","images/ok.jpg");
    }
    if(numQuestions==1&&another){//if there were 2 questions, but remains 1
        info.innerText = "Correcto, responde la segunda pregunta";
        selectQ = randGen(long);
        question.innerText = questions[selectQ][0]+"\n";
        question.innerText+= `A) ${questions[selectQ][1]} 
        B) ${questions[selectQ][2]}\n C) ${questions[selectQ][3]}
        D) ${questions[selectQ][4]}`;
    }
})
///////
// reload event:
reload.addEventListener("click",()=>location.reload());