"use strict";
const printSpiral = size=>{
    if(typeof(size)=="number"&&size>=2){
        size = Math.floor(size);
        const h='═',v='║',rd='╗',ur='╔',ru='╝',dr='╚';
        let str = "";
        str+= "".padEnd(size-1,h)+rd+"\n";
        for(let i=1;i<size-1;i++){
            if(i<Math.floor(size/2)){
                str+="".padEnd(i-1,v)+ur+"".padEnd(size-2*i-1,h)+rd+"".padEnd(i,v)+"\n";
            }else if(i==Math.floor(size/2)&&size%2==1){ 
                str+="".padEnd(Math.floor(size/2)-1,v)+ur+rd+"".padEnd(Math.floor(size/2),v)+"\n";
            }else{
                str+="".padEnd(size-1-i,v)+dr+"".padEnd(2*i-size,h)+ru+"".padEnd(size-1-i,v)+"\n";
            }
        }
        str+= dr+"".padEnd(size-2,h)+ru+"\n";
        console.log(str);
        return str;
    }else{
        console.log("el tamaño debe ser mayor a 2");
        return null;
    }
}