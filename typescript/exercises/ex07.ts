// Exercise 7: Advanced Types (Union and Intersection)
// Objective: Use union and intersection types to work with more complex type scenarios.

type inputType = string | number | HTMLElement | undefined | null;
type validInput = number | boolean;

let userInput: inputType = document.getElementById("#input");


function verifyInputEntrance(userInput: inputType): validInput {
    if ( userInput === undefined || userInput === null ) { return false; }

    return true;
}