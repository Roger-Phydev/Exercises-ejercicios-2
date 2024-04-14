"use strict";
const missedChar = (firstString,secondString)=>{
    if(typeof(firstString)=="string"&&typeof(secondString)=="string"){
        if(firstString.length==secondString.length){
            firstString = firstString.split("");
            secondString = secondString.split("");
            let missed = [];
            for(let i in firstString){
                if(firstString[i]!=secondString[i]){
                    missed.push(secondString[i]);
                }
            }
            return missed;
        }else{
            console.log("nada que hacer, no son tan similares");
            return false;
        }
    }else{
        console.log("debes introducir dos cadenas");
    }
}