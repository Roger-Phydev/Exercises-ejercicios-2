const generatePassword = (size,capitalAllow=false,numberAllow=false,symbolsAllow=false)=>{
    if(typeof(size)=="number"&&size<17&&size>=8){
        size = parseInt(size);
        let options = [];
        for (let i=97;i<123;i++){
            options.push(String.fromCharCode(i));
            if(capitalAllow){
                options.push(String.fromCharCode(i-32));
            }
            if(numberAllow&&i<107){
                options.push(String.fromCharCode(i-49));
            }
            if(symbolsAllow&&i==110){
                options.push("%","$","@","ñ","?","¿","!","¡");
            }
        }
        let l = options.length;
        let password="";
        for(let j=0;j<size;j++){
            let r = Math.round(l*Math.random()-0.5);
            password+=options[r];
        }
        return password;
    }else{
        return "el tamaño debe ser un número entre 8 y 16"
    }
}