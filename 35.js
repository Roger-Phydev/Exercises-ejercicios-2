"use strict";
const randProba = probabilityInPercent=>{
    let s = Math.round(-0.5+100*Math.random());
    if(s<=probabilityInPercent){
        return true;
    }else{
        return false;
    }
}
const WheaterSim = (numOfDays,TempInitial,RainRateInitial)=>{
    if(typeof(numOfDays)!="number"||!Number.isInteger(numOfDays)||numOfDays<1||
    typeof(TempInitial)!="number"||TempInitial<-273.15||typeof(RainRateInitial)!="number"||
    RainRateInitial<0||RainRateInitial>100){
        console.log("Debes introducir una cantidad de días, mayor a 1, entero. La temperatura debe ser mayor a -273.15 y la probabilidad de lluvia debe estar entre 0 y 100");
        return null;
    }
    let WheatherForecast = [];
    let T=TempInitial,Tm = TempInitial,TM = TempInitial;
    let RainRate = RainRateInitial,RainDays = 0;
    let Tbefore = TempInitial,RainRateBefore=RainRateInitial;
    for(let i=1;i<=numOfDays;i++){
        if(RainRateBefore==100){
            T--;
            RainDays++;
        }
        if(Tbefore>25){
            RainRate+=20
            if(RainRate>100){
                RainRate=100;
            }
        }
        if(Tbefore<5){
            RainRate-=20
            if(RainRate<0){
                RainRate=0;
            }
        }
        if(randProba(10)){
            T+=2;
        }
        Tbefore = T;
        RainRateBefore = RainRate;
        Tm = Math.min(Tm,T);
        TM = Math.max(TM,T);
        WheatherForecast.push([T,RainRate]);
    }
    console.log(`Hubieron ${RainDays} días de lluvia, con temperatura máxima de ${TM} y mínima de ${Tm}`)
    return [WheatherForecast,TM,Tm,RainDays];
}