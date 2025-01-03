let username = 'admin'
console.log(username)

let a: number = 12
let b: string = "6"
let c : number= 2


if(isNaN(Number(a)) || isNaN(Number(b)) || isNaN(Number(c))){
    console.log("Impossible to calculate because one of the variables is not a number!")
}else {
    console.log(a / Number(b) * 2) 
}