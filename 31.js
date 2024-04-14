"use strict";
const pithagoricTripletsLessThan = max=>{
    if(typeof(max)=="number"&&Number.isInteger(max)){
        if(max<5){
            return [];
        }else{
            let triplets = [];
            for(let i=5;i<=max;i++){
                for(let j=Math.ceil(i/Math.sqrt(2));j<i;j++){
                    let a = Math.sqrt(i**2 - j**2);
                    if(Number.isInteger(a)){
                        triplets.push([a,j,i]);
                    }
                }
            }
            return triplets;
        }
    }else{
        console.log("debes meter un número entero como valor");
        return [];
    }
}