"use strict"
const friday13th = (month,year)=>{
    const months = {
        "january":0,
        "february":1,
        "march":2,
        "april":3,
        "may":4,
        "june":5,
        "july":6,
        "august":7,
        "september":8,
        "october":9,
        "november":10,
        "december":11,
        "enero":0,
        "febrero":1,
        "marzo":2,
        "abril":3,
        "mayo":4,
        "junio":5,
        "julio":6,
        "agosto":7,
        "septiembre":8,
        "octubre":9,
        "noviembre":10,
        "diciembre":11
    }
    if(typeof(year)=="number"&&year==Math.floor(year)&&["number","string"].includes(typeof(month))){
        if(typeof(month)=="string"){
            month = month.toLowerCase();
        }
        if(months[month]!=undefined){
            month=months[month];
        } else if(typeof(month)=="number"&&month==Math.floor(month)&&month<13&&month>=1){
            month--;
        }else{
            console.log("error en el formato, asegurate haber introducido un mes válido");
            return null;
        }
        let date = new Date(year,month,13);
        if(date.getDay()==5){
            return true;
        }else{
            console.log(date.getDay());
            return false;
        }
    }else{
        console.log("error de formato, solo se permite introducir el mes como número o como cadena y el año como número");
        return null;
    }
}
console.log(friday13th(3,1997));