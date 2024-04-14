"use strict";
const rgbHexConversor = (color)=>{
    const conv = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"];
    if(typeof(color)=="string"&&color.startsWith("#")&&(color.length==4||color.length==7)){
        let exp = [],rgb = [];
        if(color.length==4){
            exp = [color[1],color[2],color[3]];
        }else{
            exp = [color.substring(1,3),color.substring(3,5),color.substring(5,7)];
        }
        for(let q of exp){
            let s = q.split("");
            let r = 0;
            for(let i in s){
                if(!conv.includes(s[i])){
                    console.log("debes poner tres números hexagesimales:ej #AC4523, #3FC");
                    return null;
                }
                r+=(conv.indexOf(s[i]))*((16)**(s.length-i-1));
            }
            rgb.push(r);
        }
        return rgb;
    }
    else if(Array.isArray(color)&&color.length==3&&Number.isInteger(color[0])&&Number.isInteger(color[1])&&Number.isInteger(color[2])){
        let hex = "#";
        for(let c of color){
            if(c<0||c>255){
                console.log("En caso rgb, debes poner números entre 0 y 255");
                return null;
            }
            hex+= conv[Math.floor(c/16)]+conv[c%16];
        }
        return hex;
    }else{
        console.log("debes introducir una expresión de un color.\nej: [230,1,45] (RGB), #89005A (HEX), #AF3 (HEX)");
        return null;
    }
}