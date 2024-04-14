"use strict"
/*
This file needs the file Magichat.html which is at the repository "Retos_python_2"
*/
const first = document.querySelectorAll(".one");
const second = document.querySelectorAll(".two");
const third = document.querySelectorAll(".three");
const btn = document.getElementById("ok");
const cont = document.getElementById("res");
let ans = ["","",""];
first.forEach((option,i)=>{
    option.addEventListener("change",()=>{
        if(option.checked){
            ans[0]=option.value;
            for(let j=0;j<4;j++){
                if(j!=i){
                    first[j].checked=false;
                }
            }
        }else{
            ans[0]="";
        }
    })
});
second.forEach((option,i)=>{
    option.addEventListener("change",()=>{
        if(option.checked){
            ans[1]=option.value;
            for(let j=0;j<4;j++){
                if(j!=i){
                    second[j].checked=false;
                }
            }
        }else{
            ans[1]="";
        }
    })
});
third.forEach((option,i)=>{
    option.addEventListener("change",()=>{
        if(option.checked){
            ans[2]=option.value;
            for(let j=0;j<4;j++){
                if(j!=i){
                    third[j].checked=false;
                }
            }
        }else{
            ans[2]="";
        }
    })
});
btn.addEventListener("click",e=>{
    e.preventDefault();
    if(ans.includes("")){
        alert("Debes seleccionar una opción en cada pregunta");
    }else{
        let options = [];
        let l = -1;
        console.log(ans);
        ["g","h","r","s"].forEach(val=>{
            let c = 0;
            ans.forEach(e=>{
                if(e==val){
                    c++;
                }
            });
            console.log(c,val);
            if(c==l){
                options.push(val);
                l = c;
            }else if(c>l){
                options = [val];
                l = c;
            }
        });
        const names = {
            "g":"Griffindor",
            "h":"Humblepuff",
            "r":"Ravenclown",
            "s":"Slitterin"
        }
        if(options.length==1){
            cont.textContent = `Está decidido, debe ir a ${names[options[0]]}`;
        }else if(options.length==2){
            cont.textContent = `Estoy un poco dudoso, tus opciones son: ${names[options[0]]} o ${names[options[1]]}`;
        }else{
            cont.textContent = `Estoy un poco dudoso, tus opciones son: ${names[options[0]]} , ${names[options[1]]} o ${names[options[2]]}`;
        }
    }
    first.forEach(e=>e.checked=false);
    second.forEach(e=>e.checked=false);
    third.forEach(e=>e.checked=false);
})