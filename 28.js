"use strict";
const permutationsOf = word=>{
    if(typeof(word)=="string"&&word.match(/\w+/)!=null&&word.match(/\w+/).input==word){
        let permutations = [""];
        while(permutations[0].length<word.length){
            let add = [];
            for(let element of permutations){
                let rest = word;
                for(let l of element){
                    rest = rest.replace(l,"");
                }
                for(let r of rest){
                    add.push(element+r);
                }
            }
            permutations = add;
        }
        return permutations;
    }else{
        console.log("debes introducir una palabra",word.match(/\w+/));
    }
}