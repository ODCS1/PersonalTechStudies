// Exercise 2: Functions with Type Annotations
// Objective: Define functions that take arguments with specific types and return values of a specific type.


// 1º
function allName(arr: string[]): string {
    let output: string = "";

    if (!Array.isArray(arr) || arr.length === 0){ return output; }

    for (let i = 0; i < arr.length; i++) {
        if (i < arr.length - 1) { output += `${arr[i]} - `; continue; }

        output += `${arr[i]}!`
    }


    return output;
}


// 2º

const WORD:string = "a";

type numberOrString = number | string;

let numberOrString = function(val: numberOrString): string {
    if (typeof val === "string") { return "NOT A NUMBER!!"; }
    return "NUMBER!!";
}

console.log(numberOrString(WORD));



// 3º
type mixArrayType = (number | string)[];

let isValidArray = (arr: mixArrayType):boolean => {
    if ( arr.length === 0 ) { return false; }

    for (let i = 0; i < arr.length; i++){
        if (arr[i] === undefined) { return false; }
    }

    return true;
}


// 4º
const isNumber = (value: any): boolean => {
    return typeof value === "number"
            ? true
            : false;
}

console.log(isNumber(2754));