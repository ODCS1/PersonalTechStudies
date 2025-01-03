"use strict";
var username = 'admin';
console.log(username);
var a = 12;
var b = "6";
var c = 2;
if (isNaN(Number(a)) || isNaN(Number(b)) || isNaN(Number(c))) {
    console.log("Impossible to calculate because one of the variables is not a number!");
}
else {
    console.log(a / Number(b) * 2);
}
