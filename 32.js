"use strict";
const multTableOf = num=>{
    if(typeof(num)=="number"&&Number.isInteger(num)&&num<11&&num>0){
        for(let i =1;i<=10;i++){
            console.log(`${num} x ${i} = ${num*i}`);
        }
        return num;
    }else{
        console.log("Debes introducir un valor entre 1 y 10");
        return null;
    }
}