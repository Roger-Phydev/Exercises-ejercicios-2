"use strict";
const printTriforce = size=>{
    if(typeof(size)=="number"&&size==Math.floor(size)&&size>1){
        let str = "";
        for(let i=1;i<=size;i++){
            str+="".padEnd(2*size-i," ")+"".padEnd(2*i-1,"* ")+"".padEnd(2*size-i," ")+"\n";
        }
        for(let i=1;i<=size;i++){
            str+="".padEnd(size-i," ")+"".padEnd(2*i-1,"* ")+"".padEnd(size-i," ")+" "+"".padEnd(size-i," ")+"".padEnd(2*i-1,"* ")+"".padEnd(size-i," ")+"\n";
        }
        console.log(str);
        return str;
    }else{
        console.log("el tamaño debe ser entero y mayor que 1");
        return null;
    }
}