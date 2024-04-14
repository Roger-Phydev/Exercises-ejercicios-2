"use strict";
/*
This file needs the file rsp.html which is at the repository "Retos_python_2"
*/
const RandGen = long=>{
    return Math.round(-0.5+long*Math.random());
}
const score = document.getElementById("stat");
const screen = document.getElementById("screen");
const chose = document.getElementById("zone");
const reload = document.getElementById("reload");
let a=0,b=0,win="";
let options = ["Piedra","Papel","Tijeras"];
let wins = [["Piedra","Tijeras"],["Papel","Piedra"],["Tijeras","Papel"]];
chose.lastElementChild.addEventListener("click",()=>{
    let player = chose.firstElementChild.value;
    let cpu = options[RandGen(3)];
    if(wins.some(val=>val[0]==player&&val[1]==cpu
    )){
        win = "jugador";
        a++;
    }else if(wins.some(val=>val[0]==cpu&&val[1]==player
    )){
        win = "CPU"
        b++;
    }else{
        win= "";
    }
    score.innerText= `Marcador: ${a}-${b}`;
    if(win!=""){
        screen.innerText = `tú:${player}\ncpu:${cpu}\n
        ${win} ha ganado la ronda. A jugar la siguiente:`;
    }else{
        screen.innerText = `tú:${player}\ncpu:${cpu}\n
        Ronda empatada. Continuamos la siguiente ronda`;
    }
    if(a==2||b==2){
        screen.innerText= `${win} ha ganado la partida`;
        zone.style = "display: none;";
        reload.style = "display: block;";
    }
});
reload.addEventListener("click",()=>{
    location.reload();
})