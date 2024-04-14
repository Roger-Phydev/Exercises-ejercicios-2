"use strict";
const isPrime = n=>{
    if(n<2){
        return false;
    }
    for(let i=2;i<Math.floor(n/2);i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}
const twinPrimesInRange = max=>{
    if(typeof(max)=="number"&&max==Math.floor(max)){
        if(max<5){
            return [];
        }else{
            let ans = [];
            for(let j=5;j<=max;j++){
                if(isPrime(j)&&isPrime(j-2)){
                    ans.push([j-2,j]);
                }
            }
            return ans;
        }
    }
}