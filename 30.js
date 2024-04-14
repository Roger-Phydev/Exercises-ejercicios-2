"use strict";
const allOptionsToSumIn = (numberArray,target) =>{
    if(Array.isArray(numberArray)&&typeof(target)=="number"&&Number.isInteger(target)){
        if(target<=0){
            return [];
        }
        for(let i of numberArray){
            if(typeof(i)!="number"||!Number.isInteger(i)||i<=0){
                console.log("asegurate que el array está conformado por números enteros positivos");
                return [];
            }
        }
        if(numberArray.reduce((total,num)=>total+num,0)<target){
            return [];
        }else if(numberArray.reduce((total,num)=>total+num,0)==target){
            numberArray.sort((a,b)=>a-b);
            return numberArray;   
        }
        numberArray.sort((a,b)=>b-a);
        let construction = [[]], posibilities = [];
        for(let i in numberArray){
            if(numberArray[i]>target){
                continue;
            }else if(numberArray[i]==target){
                posibilities.push([numberArray[i]])
                continue;
            }else{
                construction.forEach(e=>{
                    if(e.concat(numberArray[i]).reduce((total,item)=>total+item,0)<target){
                        construction.push(e.concat(numberArray[i]))
                    }else if(e.concat(numberArray[i]).reduce((total,item)=>total+item,0)==target){
                        let add = e.concat(numberArray[i]);
                        add.sort((a,b)=>a-b);
                        if(!posibilities.some(subArray=>subArray.length===add.length&&subArray.every((value,index)=>value===add[index]))){
                            posibilities.push(add);
                        }
                    }
                }) 
                }
            }
        return posibilities;
    }else{
        console.log("Asegurate de introducir un array y un número entero");
        return null;
    }
}