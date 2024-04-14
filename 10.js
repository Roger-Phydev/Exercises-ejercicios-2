"use strict"
const urlParameters = urlString =>{
    if(typeof(urlString)=="string"){
        let finds = urlString.matchAll(/(?<=\=)\w+(?=\&|$)/g);
        let a = [];
        for(let r of finds){
            a.push(r[0]);
        }
        return a;
    }
}