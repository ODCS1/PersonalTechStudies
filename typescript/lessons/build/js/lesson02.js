"use strict";
// INFERENCE - Typescript verifies the type based on the value assigned to the variable
// This type is implicit, you can´t change it assigning a new value of a different type to the variable.
var l2_text1 = "some text to check type";
// EXPLICIT
var l2_text2 = "Explicit text.";
var l2_myName = "Prinsk";
var l2_meaningOfLife;
var l2_isLoading;
var l2_album;
var l2_numberOrString = "text";
l2_myName = "Kartorstr";
l2_meaningOfLife = 92;
l2_isLoading = true;
l2_album = "Tasrteskin";
l2_numberOrString = prompt("l2_numberOrString: ") || "";
var sum = function (l2_a, l2_b) {
    return l2_a + l2_b;
};
if (!isNaN(Number(l2_numberOrString)) && l2_numberOrString !== "") {
    console.log("SUM: ".concat(sum(Number(l2_numberOrString), 7)));
}
else {
    console.log("The current value assignment to the variable is not a number!");
}
var postId;
var isActive;
var re = /\w+/g;
