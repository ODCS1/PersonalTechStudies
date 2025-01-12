// Exercise 11: Optional and Default Parameters
// Objective: Learn how to work with optional and default parameters in TypeScript.


let calculate = (a: number, b: number, op:string="+", times?:number):number => {

    let output = -1;
    switch (op) {
        case "+":
            output = a + b;
        case "-":
            output = a - b;
        case "*":
            output = a * b;
        case "/":
            if (b != 0) { output = a / b; }
        case "^":
            output = a * b;
    }

    if (typeof times !== "undefined") { output *= times; }
    return output;
}


console.log("Result: " + calculate(2, 5, "*"));