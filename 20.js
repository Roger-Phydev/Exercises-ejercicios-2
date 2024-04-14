"use strict";
const caesarCode = (text,uncode=false,space=4)=>{
    if(typeof(text)=="string"){
        if(uncode==false){
            text = text.split("");
            for(let i in text){
                if(text[i].charCodeAt()>=65&&text[i].charCodeAt()<92){
                    text[i]=String.fromCharCode(65+(text[i].charCodeAt()-65+space)%26);
                }else if(text[i].charCodeAt()<124&&text[i].charCodeAt()>96){
                    text[i]=String.fromCharCode(97+(text[i].charCodeAt()-97+space)%26);
                }
            }
            return text.join("");
        }else{
            text = text.split("");
            for(let i in text){
                if(text[i].charCodeAt()>=65&&text[i].charCodeAt()<92){
                    text[i]=String.fromCharCode(65+(26+text[i].charCodeAt()-65-space)%26);
                }else if(text[i].charCodeAt()<124&&text[i].charCodeAt()>96){
                    text[i]=String.fromCharCode(26+97+(text[i].charCodeAt()-97-space)%26);
                }
            }
            return text.join("");
        }
    }
}