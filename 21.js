"use strict";
let input = [];
let code = "ArrowUpArrowUpArrowDownArrowDownArrowLeftArrowRightArrowLeftArrowRightba";
addEventListener("keyup",k=>{
    input.push(k.key);
    console.log(input,code);
    if(input.length>10){
        input.shift();
        console.log(input.join(""),code);
        if(input.join("")==code){
            document.write("Excelente, lograste el código konami");
        }
    }
})