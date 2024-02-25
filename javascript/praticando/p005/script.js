corCabelo = str(window.prompt('Qual a cor do seu cabelo: '))

if (cor === 'preto'){
    let c = 1
    while(c <= 10){
        print(`${c} ${cor}`)
        c++
    }
}else if(cor === 'loiro'){
    let c = 1
    do{
        print(`${c} ${cor}`)
    }while(c <= 5)
}else if(cor === 'castanho'){
    for(let c = 1; c <= 3; c++){
        print(`${c} ${cor}`)
    }
}else if(cor === 'ruivo'){
    for(let c = 1; c <= 2; c++){
        print(`${c} ${cor}`)
    }
}else{
    print(`${cor}`)
}