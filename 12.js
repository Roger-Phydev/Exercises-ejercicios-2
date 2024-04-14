"use strict"
/*
This file needs the file words.html which is at the repository "Retos_python_2"
*/
const GenRandomValue = (final)=>{
    return Math.round(-0.5+final*Math.random());
}
const selection = document.getElementById("difficult");
const show = document.getElementById("word");
const screen = document.getElementById("status");
const zone = document.getElementById("area");
const reset = document.getElementById("reload");
const words = ["ventilador","favorito","murcielago","dormitorio","armadillo","violencia","videojuego","computadora","ornitorrinco","camaraderia"];
let word = words[GenRandomValue(words.length)].split("");
let diff = "", n = 0;
let win = false;
let showed,keys=[],letters=[];
selection.lastElementChild.addEventListener("click",()=>{
    diff = selection.children[0].value;
    n = parseInt(selection.children[3].value);
    let h = 0;
    selection.style = "display: none;";
    if(diff=="Fácil"){
        h = Math.floor(word.length/4);
    }else if(diff=="Normal"){
        h = Math.floor(word.length/2)-1;
    }else{
        h = Math.floor(word.length/2)+1;
    }
    while(keys.length<h){
        let i = GenRandomValue(word.length);
        if(keys.indexOf(i)==-1){
            keys.push(i);
            letters.push(word[i]);
        }
    }
    showed = word.map((val,i)=>{
        if(keys.indexOf(i)!=-1){
            return "_";
        }else{
            return val;
        }
    });
    show.style = "display: block;";
    show.innerText = showed.join(" ");
    screen.innerText = "Introduce una letra o prueba adivinar la palabra"+`\n intentos:${n}`;
    zone.style = "display = block"; 
});
zone.lastElementChild.addEventListener("click",()=>{
    let ans = zone.firstElementChild.value;
    if(ans==word.join("")){
        screen.innerText = `Muy bien, ganaste, la palabra era: ${word.join("")}`;
        show.innerText = word.join(" ");
        zone.style = "display : none;";
        reset.style = "display : block;";
    }else if(letters.indexOf(ans)!=-1){
        let j = letters.indexOf(ans);
        showed[keys[j]]=letters[j];
        letters.splice(j,1);
        keys.splice(j,1);
        show.innerText = showed.join(" ");
        zone.firstElementChild.value="";
    }else{
        n--;
        screen.innerText = "Introduce una letra o prueba adivinar la palabra"+`\n intentos:${n}`;
        zone.firstElementChild.value="";
    }
    if(letters.length==0){
        screen.innerText = `Muy bien, ganaste, la palabra era: ${word.join("")}`;
        zone.style = "display : none;";
        reset.style = "display : block;";
    }
    if(n<=0){
        screen.innerText = `Perdiste, la palabra era: ${word.join("")}`;
        zone.style = "display : none;";
        reset.style = "display : block;";
    }
})
reset.addEventListener("click",()=>{
    location.reload();
})