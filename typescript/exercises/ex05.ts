// Exercise 5: Generics
// Objective: Write a generic function to return the first element of an array.

let genericFunction = <T>(x: T[]):T => {
    return x[0];
}

let arr:string[] = ["op", "hsk", "nipriskt"];
console.log(genericFunction(arr));