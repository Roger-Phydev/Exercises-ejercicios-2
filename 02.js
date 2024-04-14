const newScore = (winnerScore,looserScore)=>{
    if(winnerScore=="Love"){
        return "15";
    }else if (winnerScore=="15"){
        return "30";
    }else if (winnerScore=="30" && looserScore!="40"){
        return "40";
    }else if (winnerScore=="30" && looserScore=="40"){
        return "deuce";
    }else if (winnerScore=="40" && looserScore=="advantage"){
        return "deuce";
    }else if (winnerScore=="40" && looserScore!="advantage"){
        return "advantage";
    }else if (winnerScore=="deuce"){
        return "advantage";
    }else if (winnerScore=="advantage"){
        return "win";
    }
}
const countIn = (array,expression) =>{
    let n=0;
    for(l of array){
        if(l==expression){
            n++
        }
    }
    return n;
}
const tennisMatch = winnerList =>{
    if(Array.isArray(winnerList)&&countIn(winnerList,"P1")+countIn(winnerList,"P2")==winnerList.length){
        let playerOne = "Love", playerTwo = "Love";
        for(winner of winnerList){
            if(winner=="P1"&&playerOne!="win"){
                playerOne = newScore(playerOne,playerTwo);
                if(playerOne=="advantage"){
                    playerTwo="40";
                }else if(playerOne=="deuce"){
                    playerTwo="deuce";
                }
                console.log(` P1  P2 \n${playerOne} - ${playerTwo}`);
                if(playerOne=="win"){
                    return "P1 wins";
                }
            }else if(winner=="P2"&&playerTwo!="win"){
                playerTwo = newScore(playerTwo,playerOne);
                if(playerTwo=="advantage"){
                    playerOne="40";
                }else if(playerTwo=="deuce"){
                    playerOne="deuce";
                }
                console.log(` P1  P2 \n${playerOne} - ${playerTwo}`);
                if (playerTwo=="win"){
                    return "P2 wins";
                }
            }
        }
    }else{
        return "debes introducir un arreglo con solo expresiónes 'P1' o 'P2'";
    }
}
console.log(tennisMatch("sdsad"));
console.log(tennisMatch([1,2,1]));
console.log(tennisMatch(["P1",2,2]));
console.log(tennisMatch(["P1","P1","P2","P2","P1","P2","P1","P1"]));
console.log(tennisMatch(["P1","P1","P1","P2","P2","P2","P2","P1","P1","P1","P1","P2","P2","P2"]));
console.log(tennisMatch(["P1","P2","P1","P1","P2","P2","P1","P2","P2","P2","P1"]));