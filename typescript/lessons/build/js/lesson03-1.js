"use strict";
// OBJECTS
// 1 - BASIC OBJECT SYNTAX
const person = {
    name: "John",
    age: 30,
    weight: 91.76,
};
const person2 = {
    name: "Trold",
    age: 92,
    weight: 76,
};
const person3 = {
    name: "Bobirson",
    age: 34,
    weight: 81,
};
const car = {
    make: "Tesla",
    model: "Model S",
};
const book = {
    title: "1984",
    author: "George Orwell",
};
const translations = {
    hello: "Olá",
    world: "mundo",
};
console.log(translations["hello"] + ", " + translations["world"] + "!");
// 6 - METHODS IN OBJECTS
/**
 * OBJECTS CAN ALSO CONTAIN FUNCTIONS AS PROPERTIES, KNOWN AS
 * MWTHODS
 */
const calculator = {
    add: (a, b) => a + b,
    subtract(a, b) {
        return a - b;
    },
};
console.log(`SUM: ${calculator.add(1, 2)} - SUB: ${calculator.subtract(4, 1)}`);
const dog1 = {
    name: "Buddy",
    breed: "Pincher",
};
const human = { name: "Eve", age: 20 };
const pet = {
    bark: () => console.log("Woof"),
};
// 9 -  OBJECT MANIPULATION
/**
 * MANIPULATE OBJECTS USING BUILT-IN METHODS SUCH AS Object.keys,
 * Object.values and Object.entries (ES2017+)
 */
const user = { id: 1, name: "Alice", role: "admin" };
console.log(Object.keys(user)); // ["id", "name", "role"]
console.log(Object.values(user)); // [1, "Alice", "admin"]
console.log(Object.entries(user)); // [["id", 1], ["name", "Alice"], ["role", "admin"]]
// 10 - CLASSES AS OBJECTS
/**
 * CLASSES IN TYPESCRIPT CREATE OBJECTS WITH ADDITIONAL
 * FEATURES LIKE ENCAPSULATION AND INHERITANCE.
 */
class Person4 {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    gret() {
        console.log(`Hello, my name is ${this.name}`);
    }
}
const p = new Person4("Jonny", 31);
p.gret();
