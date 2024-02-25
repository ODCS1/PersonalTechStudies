let nome = prompt('Nome: ')
let idade = prompt('Idade: ')
let gen = prompt('Genêro: ')

if (gen === 'h'){
    if(idade < 18){
        console.log('Se prepare para se alistar no exército.')
    } else if(idade === 18){
        console.log('Não se esqueça do Alistamento Militar este ano.')
    } else{
        console.log('Caso não tenha realizado o alistamento militar, regularize o quanto antes.')
    }
} else{
    console.log('O alistamento militar obrigatório não é necessário para mulheres, caso queira ingressar em uma das 3 forças, preste um concurso militar de seu interesse.')
}