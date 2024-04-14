"use strict";
const excelColumnNumber = columExpression =>{
    if(typeof(columExpression)=="string"){
        let num = 0;
        let mult = 26**(columExpression.length-1);
        for(let l of columExpression){
            if(l.charCodeAt()<65||l.charCodeAt()>90){
                console.log("asegurate de que tu expresión solo contiene letras A-Z, ej: AA, ACA");
                return null;
            }else{
                num+=(l.charCodeAt()-64)*mult;
                mult=mult/26;
            }
        }
        return num;
    }else{
        console.log("debes introducir una cadena");
        return null;
    }
}