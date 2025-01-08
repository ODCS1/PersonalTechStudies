"use strict";
// LITERAL TYPES
let myName;
let userName;
userName = "Amy";
// FUNCTIONS
const add = (a, b) => {
    return a + b;
};
const logMsg = (message) => {
    console.log(message);
};
logMsg("Hello!");
logMsg(add(2, 3));
let subtract = function (c, d) {
    return c - d;
};
// interface mathFunction {
//     (a: number, b: number): number;
// }
let multiply = function (c, d) {
    return c * d;
};
logMsg(multiply(2, 2));
// OPTIONAL PARAMETES
const addAll = (a, b, c) => {
    if (typeof c !== "undefined") {
        return a + b + c;
    }
    return a + b;
};
// DEFAULT PARAM VALUE
const sumAll = (a = 10, b, c = 2) => {
    return a + b + c;
};
logMsg(addAll(2, 3, 2));
logMsg(addAll(2, 3));
logMsg(sumAll(2, 3));
logMsg(sumAll(undefined, 3));
// REST PARAMETERS
let total = function (a, ...nums) {
    return nums.reduce((total, num) => total + num, a);
};
logMsg(total(10, 2, 3));
const createError = (errMsg) => {
    throw new Error(errMsg);
};
const infinite = () => {
    let i = 1;
    while (true) {
        i++;
        // if (i == 5) break; // void
    }
};
// CUSTOM TYPE GUARD
const isNumber = (value) => {
    return typeof value === "number"
        ? true
        : false;
};
// USE OF THE NEVER TYPE
const numberOrString = (value) => {
    if (typeof value === "string")
        return "string";
    if (typeof value === "number")
        return "number";
    return createError("THIS SHOULD NEVER HAPPEN!");
};
