"use strict";
let l1_username = "admin";
console.log(l1_username);
let l1_a = 12;
let l1_b = "6";
let l1_c = 2;
if (isNaN(Number(l1_a)) || isNaN(Number(l1_b)) || isNaN(Number(l1_c))) {
    console.log("Impossible to calculate because one of the variables is not a number!");
}
else {
    console.log((l1_a / Number(l1_b)) * 2);
}