// Exercise 9: Arrays and Tuples
// Objective: Create arrays and tuples, and practice accessing their values.

let myTuple: [string, number, boolean];
myTuple = ["text", 1, true];

console.log(myTuple[0] + "==" + myTuple["text"]);

// TRYING TO ASSIGNING AN INVALIS TYPE
// myTuple = ["text", 4, "false"];
// myTuple[0] = true;

let body: string[] = ["skin", "head", "elbow", "knee"];
body[0] = "hair";
body[1] = "belly";

// WRONG TYPE ASSIGNING
// body[3] = true;

let values: number[] = [2, 3, 4, 5, 6, 7, 2];



function calculateEarlyValue(arr: number[]) {
    if (Array.isArray(arr) && arr.length < 2) { return; }

    let curr_value = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (i > 0) {
            arr[i] *= curr_value;
        }
    }
}


calculateEarlyValue(values)
console.log(values);