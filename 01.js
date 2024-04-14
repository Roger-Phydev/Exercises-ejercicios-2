"use strict"
const coding = {
    "a":"4",
    "b":"l3",
    "c":"[",
    "d":")",
    "e":"3",
    "f":"|=",
    "g":"&",
    "h":"#",
    "i":"1",
    "j":",_|",
    "k":">|",
    "l":"7",
    "m":'/V\ ',
    "n":"^/",
    "o":"0",
    "p":"|*",
    "q":"(_,)",
    "r":"I?",
    "s":"5",
    "t":"+",
    "u":"(_)",
    "v":"\/",
    "w":"VV",
    "x":"><",
    "y":"`/",
    "z":"2",
    "1":"L",
    "2":"R",
    "3":"E",
    "4":"A",
    "5":"S",
    "6":"b",
    "7":"T",
    "8":"B",
    "9":"g",
    "0":"o"
};
const toHacker = str=>{
    if(typeof(str)=="string"){
        str = str.toLowerCase();
        let coded = "";
        for(let l of str){
            if(coding[l]!=undefined){
                coded+=coding[l];
            }else{
                coded+=l;
            }
        }
        return coded;
    }
};
const a = "RogEr1 Parra";
console.log(a,toHacker(a));