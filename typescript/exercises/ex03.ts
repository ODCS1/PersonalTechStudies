// Exercise 3: Interfaces and Types
// Objective: Define an interface for a Person object and create an object that adheres to that interface.

interface Person {
    name: string;
    age: number;
    weight: number;
    height: number;
    greet(): string;
}


let person1: Person = {
    name: "Agístósvrirt",
    age: 93,
    weight: 63,
    height: 1.72,
    greet() {
        return `Hi, my name is ${this.name} and i have ${this.age} years old.`;
    },
}