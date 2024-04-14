"use strict";
const collideTime = (positionOne,positionTwo,velocityOne,velocityTwo)=>{
    if(Array.isArray(positionOne)&&Array.isArray(positionTwo)&&Array.isArray(velocityOne)&&Array.isArray(velocityTwo)&&
    positionOne.every(e=>typeof(e)=="number")&&positionTwo.every(e=>typeof(e)=="number")&&
    velocityOne.every(e=>typeof(e)=="number")&&velocityTwo.every(e=>typeof(e)=="number")&&
    positionOne.length==positionTwo.length&&positionTwo.length==velocityOne.length&&
    velocityOne.length==velocityTwo.length&&positionOne.length>1){
        let l = positionOne.length;
        let diffP = positionTwo.map((val,i)=>val-positionOne[i]);
        if(diffP.every(e=>e==0)){
            console.log("no hay colisión");
            return null;
        }
        let diffV = velocityTwo.map((val,i)=>val-velocityOne[i]);
        if(diffV.every(e=>e==0)){
            console.log("no hay colisión, son líneas paralelas");
            return null;
        }
        if(l==2){
            let pdP = diffV.reduce((total,val,i)=>total+val*diffP[i],0);
            let pdC = diffP[0]*diffV[1]-diffV[0]*diffP[1];
            if(pdC==0&&pdP<0){
                let time = Math.sqrt((diffP.reduce((total,val)=>total+val**2,0))/(diffV.reduce((total,val)=>total+val**2,0)));
                let pos = positionOne.map((val,i)=>val+time*velocityOne[i]);
                console.log(`colisión en ${pos} a los ${time} segundos`);
                return time;
            }else{
                console.log("No hubo colisión");
                return null;
            }
        }else if(l==3){
            let pdP = diffV.reduce((total,val,i)=>total+val*diffP[i],0);
            let pdC = [diffP[1]*diffP[2]-diffP[2]*diffV[1],diffP[2]*diffV[1]-diffP[1]*diffV[2],diffP[1]*diffV[2]-diffP[2]*diffV[1]];
            if(pdC.every(e=>e==0)&&pdP<0){
                let time = Math.sqrt((diffP.reduce((total,val)=>total+val**2,0))/(diffV.reduce((total,val)=>total+val**2,0)));
                let pos = positionOne.map((val,i)=>val+time*velocityOne[i]);
                console.log(`colisión en ${pos} a los ${time} segundos`);
                return time;
            }else{
                console.log("No hubo colisión");
                return null;
            }
        }
        let time,first = true;
        diffV.forEach((val,i)=>{
            if(val!=0){
                if(first){
                    time = -(diffP[i]/val)
                    if(time<=0){
                        console.log("no hay colisión");
                        return null;
                    }
                }else{
                    if(-(diffP[i]/val)!=time){
                        console.log("no hubo colisión");
                        return null;
                    }
                }
            }
        })
        let pos = positionOne.map((val,i)=>val+time*velocityOne[i]);
        console.log(`Hubo una colisión en ${pos} al tiempo de ${time} segundos`);
        return time;
    }else{
        console.log("asegurate de meter arreglos con números de la misma longitud, mayor a 2")
        return null;
    }
}