"use strict";
const counter = (array,symbol)=>{
    let s=0;
    for(let l of array){
        if(l==symbol){
            s++;
        }
    }
    return s;
}
const abacusReader = abacusArray =>{
    if(Array.isArray(abacusArray)&&abacusArray.length==7){
        let i = 1000000;
        let total = 0;
        for(let row of abacusArray){
            if(row.length!=12||counter(row,"-")!=3||counter(row,"O")!=9||row.match(/[O]*---[O]*/)==null){
                console.log("cada fila debe tener 9 'O' separadas en algún punto por '---'");
                return false;
            }else{
                total+= i*parseInt(row.split("---")[0].length);
                i = i/10;
            }
        }
        return total;
    }else{
        console.log("Debes introducir un array de 7 elementos");
        return null;
    }
}