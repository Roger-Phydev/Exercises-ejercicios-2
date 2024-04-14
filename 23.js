"use strict";
const MathExpressions = expression=>{
    if(typeof(expression)=="string"){
        expression = expression.split(" ");
        if(expression.length%2==0||expression.length<3){
            return false;
        }else{
            for(let i in expression){
                if(i%2==0){
                    try{
                        expression[i] = parseFloat(expression[i]);
                    }catch{
                        return false;
                    }
                }else if(i%2==1&&!["+","-","*","/"].includes(expression[i])){
                    return false;
                }
            }
            return true;
        }
    }else{
        console.log("Debes meter una expresión");
    }
}