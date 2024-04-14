"use strict";
const toOctalAndHex = number=>{
    if(typeof(number)=="number"&&number==Math.floor(number)){
        const hexConv = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"];
        let oct = "", hex = "",n=number,m=number;
        while(n!=0||m!=0){
            if(n!=0){
                oct = (n%8).toString()+oct;
                n = (n-n%8)/8;
            }
            if(m!=0){
                hex = hexConv[(m%16)-1]+hex;
                m = (m-m%16)/16;
            }
        }
        return [oct,hex];
    }else{
        return null;
    }
}