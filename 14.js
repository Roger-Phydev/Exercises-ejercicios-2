"use strict";
const spanishToAurebesh = { 
    "a":"🚂",
    "b":"🚃",
    "c":"🚄",
    "d":"🚅",
    "e":"🚆",
    "f":"🚇",
    "g":"🚈",
    "h":"🚉",
    "i":"🚊",
    "j":"🚝",
    "k":"🚞",
    "l":"🚋",
    "m":"🚌",
    "n":"🚍",
    "ñ":"🚎",
    "o":"🚐",
    "p":"🚑",
    "q":"🚒",
    "r":"🚓",
    "s":"🚔",
    "t":"🚕",
    "u":"🚖",
    "v":"🚗",
    "w":"🚘",
    "x":"🚙",
    "y":"🚚",
    "z":"🚛",
};
const aurebeshToSpanish = {};
for(let key in spanishToAurebesh){
    aurebeshToSpanish[spanishToAurebesh[key]]=key;
}
const AurebeshConversor = text=>{
    if(typeof(text)=="string"){
        text = text.toLowerCase().split("");
        console.log(text);
        for(let i in text){
            if(spanishToAurebesh[text[i]]!=undefined){
                text[i]=spanishToAurebesh[text[i]];
            }else if(aurebeshToSpanish[text[i]]!=undefined){
                console.log("Ok");
                text[i]=aurebeshToSpanish[text[i]];
            }
        }
        return text.join("");
    }   
}