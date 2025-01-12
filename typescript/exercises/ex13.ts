// Exercise 15: Type Aliases
// Objective: Create custom types using type and use them in your code.

type ex13_stringOrNumber = string | number;

let age: ex13_stringOrNumber = "forty";
age = 18;

type TypePerson = {
    name: string;
    age: ex13_stringOrNumber;
    height: number;
}

let ex13_person: TypePerson = {
    name: "Giberson",
    age: 91,
    height: 1.97
}