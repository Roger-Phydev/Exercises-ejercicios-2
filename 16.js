"use strict"
const textAnalysis = text=>{
    if(typeof(text)=="string"){
        text = text.toLowerCase();
        let words = text.match(/(?<=\W|^)[a-záéíóúñ]+/g);
        let phrases = text.split(/\.+/);
        let m = "",l=0;
        for(let word of words){
            l+= (word.length)/(words.length);
            if(m.length<word.length){
                m=word;
            }
        }
        console.log(`Se obtuvo que la palabra más larga es ${m}, la longitud de palabra media es ${l} y hay ${phrases.length} frases`);
        return [m,l,phrases.length];
    }else{
        console.log("error, debes introducir una cadena");
        return null;
    }
}