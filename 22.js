"use strict";
const countdownUntilZero = (begin,seconds)=>{
    if(typeof(begin)=="number"&&typeof(seconds)=="number"&&begin>0&&Number.isInteger(begin)&&seconds>0&&Number.isInteger(seconds)){
        for(let j=begin;j>=0;j--){
            setTimeout(()=>{
                document.write(j+"\n");
            },(begin-j)*seconds*1000);
        }
        return true;
    }else{
        console.log("debes introducir un número para empezar, entero positivo y la duración en segundos");
        return null;
    }
}