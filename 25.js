"use strict";
const t9Conversor = t9string =>{
    try{
        t9string = t9string.split("-");
        let conversion={
            "1":[",",".","?","!"],
            "2":["A","B","C"],
            "3":["D","E","F"],
            "4":["G","H","I"],
            "5":["J","K","L"],
            "6":["M","N","O"],
            "7":["P","Q","R","S"],
            "8":["T","U","V"],
            "9":["W","X","Y","Z"],
            "0":[" "]
        }
        let conversed = "";
        for(let item of t9string){
            if(conversion[item[0]]==undefined){
                console.log("debes usar solo números del 0 al 9");
                return false;
            }
            if(item!="".padEnd(item.length,item[0])){
                console.log("Debes poner el mismo número seguido");
                return false;
            }else{
                let i = item.length-1%conversion[item[0]].length; //se reinicia si se pulsa de más.
                conversed+=conversion[item[0]][i];
                console.log(i);
            }
        }
        return conversed;
    }catch{
        console.log("asegurate de introducir una cadenas, además debes poner números del 0 al 9 separados por -, ej: 22-44-999");
        return null;
    }
}