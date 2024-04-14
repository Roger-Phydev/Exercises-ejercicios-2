"use strict"
const isHeterogram = text=>{
    if(typeof(text)!="string"){
        return null;
    }
    text = text.toLowerCase();
    text = text.replace(/\./g,``);
    text = text.replace(/\:/g,``);
    text = text.replace(/\;/g,``);
    text = text.replace(/\,/g,``);
    text = text.replace(/ /g,``);
    text = text.replace(/\?/g,``);
    text = text.replace(/\¿/g,``);
    text = text.replace(/\¡/g,``);
    text = text.replace(/\!/g,``);
    text = text.replace(/á/g,``);
    text = text.replace(/é/g,``);
    text = text.replace(/í/g,``);
    text = text.replace(/ó/g,``);
    text = text.replace(/ú/g,``);
    let used = [];
    for (let letter of text){
        if(!used.includes(letter)){
            used.push(letter);
        }else{
            return false;
        }
    }
    return true;
}
const isPangram = text=>{
    if(typeof(text)!="string"){
        return null;
    }
    text = text.toLowerCase();
    text = text.replace(/\./g,``);
    text = text.replace(/\:/g,``);
    text = text.replace(/\;/g,``);
    text = text.replace(/\,/g,``);
    text = text.replace(/ /g,``);
    text = text.replace(/\?/g,``);
    text = text.replace(/\¿/g,``);
    text = text.replace(/\¡/g,``);
    text = text.replace(/\!/g,``);
    text = text.replace(/á/g,``);
    text = text.replace(/é/g,``);
    text = text.replace(/í/g,``);
    text = text.replace(/ó/g,``);
    text = text.replace(/ú/g,``);
    let letters = "abcdefghijklmnopqrstuvwxyz";
    for(let l of text){
        if(letters.includes(l)){
            letters = letters.replace(l,"");
        }
    }
    if(letters==""){
        return true;
    }else{
        return false;
    }
}
const isIsogram = text=>{
    if(typeof(text)!="string"){
        return null;
    }
    text = text.toLowerCase();
    text = text.replace(/\./g,``);
    text = text.replace(/\:/g,``);
    text = text.replace(/\;/g,``);
    text = text.replace(/\,/g,``);
    text = text.replace(/ /g,``);
    text = text.replace(/\?/g,``);
    text = text.replace(/\¿/g,``);
    text = text.replace(/\¡/g,``);
    text = text.replace(/\!/g,``);
    text = text.replace(/á/g,``);
    text = text.replace(/é/g,``);
    text = text.replace(/í/g,``);
    text = text.replace(/ó/g,``);
    text = text.replace(/ú/g,``);
    let lt = [];
    let num = [];
    for (let letter of text){
        if(!lt.includes(letter)){
            lt.push(letter);
            num.push(1);
        }else{
            let i = lt.indexOf(letter);
            num[i]++;
        }
    }
    let M=0,m=text.length;
    for(let k of num){
        M = Math.max(M,k);
        m = Math.min(m,k);
    }
    if (m==M){
        return true;
    }else{
        return false;
    }
}