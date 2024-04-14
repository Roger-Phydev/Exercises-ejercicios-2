"use strict"
let r = "🗿",
p = "📄",
s = "✂️",
sp = "🖖",
l = "🦎";
const winArray = sign=>{
    if(sign==s){
        return [p,l];
    }else if(sign==p){
        return [r,sp];
    }else if(sign==l){
        return [sp,p];
    }else if(sign==sp){
        return [s,r];
    }else if(sign==r){
        return [s,l];
    }else{
        return null;
    }
};
const whoWin = playsArray=>{
    if(Array.isArray(playsArray)){
        let options = [r,p,s,sp,l];
        for (let element of playsArray){
            if(!Array.isArray(element)||element.length!=2||!([r,p,s,sp,l].includes(element[0])&&[r,p,s,sp,l].includes(element[1]))){
                return `error, el arreglo debe contener arreglos
                de dos elementos, dentro de los siguientes:
                ${r},${p},${s},${sp} o ${l}, ejemplo: [[${r},${r}],[${p},${sp}]]`;
            }
        }
        let status=0;
        for(let round of playsArray){
            if(winArray(round[0]).includes(round[1])){
                status++;
            }else if(winArray(round[1]).includes(round[0])){
                status--;
            }
        }
        if(status<0){
            return "P2 wins";
        }else if(status==0){
            return "tie";
        }else{
            return "P1 wins";
        }
    }else{
        return "debes introducir un arreglo";
    }
}
let a = [[r,s],[r,l],[sp,s],[l,s],[sp,l],[p,s],[s,p]];    
console.log(whoWin(a));