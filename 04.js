"use strict"
const isPrime = n =>{
    if(typeof(n)!="number"||n<2){
        return false;
    }
    if(n==2){
        return true;
    }
    for(let j=2;j<=Math.floor(n/2);j++){
        if(n%j==0){
            return false;
        }
    }
    return true;
}
const isFibonacci = n=>{
    if(n==0){
        return null;
    }else{
        let a=1,b=1;
        while(b<n){
            b = a+b;
            a = b-a;
        }
        if(n==b){
            return true;
        }else{
            return false;
        }
    }
}
const fibonacciPrimeEven = n=>{
    let status = `${n} `;
    if(isFibonacci(n)){
        status+="es Fibonacci";
    }else{
        status+="no es Fibonacci";
    }
    if(isPrime(n)){
        status+=", es primo";
    }else{
        status+=", no es primo";
    }
    if(n%2==0){
        status+=" y es par";
    }else{
        status+=" y es impar";
    }
    return status;
}