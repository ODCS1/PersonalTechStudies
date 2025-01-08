// OBJECTS

// 1 - BASIC OBJECT SYNTAX
const person = {
  name: "John",
  age: 30,
  weight: 91.76,
};

// 2 - OBJECT TYPES
/**
 * TYPESCRIPT ALLOWS TO DEFINE THE STRUCTURE OF OBJECTS
 * USING TYPES OR INTERFACES.THIS ENSURES TYPE SAFETY
 * AND CLARITY
 */

// USING TYPE ALIASES
type Person2 = {
  name: string;
  age: number;
  weight: number;
};

const person2: Person2 = {
  name: "Trold",
  age: 92,
  weight: 76,
};

// USING INTERFACES
interface Person3 {
  name: string;
  age: number;
  weight: number;
}

const person3: Person3 = {
  name: "Bobirson",
  age: 34,
  weight: 81,
};

// 3 - OPTIONAL PROPERTIES
interface Car {
  make: string;
  model: string;
  year?: number;
}

const car: Car = {
  make: "Tesla",
  model: "Model S",
};

// 4 - READONLY PROPERTIES
/**
 * PROPERTIES CAN BE MARKED AS READONLY TO PREVENT
 * MODIFICATION AFTER THE OBJECT IS CREATED.
 */
interface Book {
  title: string;
  readonly author: string;
}

const book: Book = {
  title: "1984",
  author: "George Orwell",
};

// 5 - INDEX SIGNATURES
/**
 * IF YOU DON´T KNOW THE PROPERTY NAMES IN ADVANCE, YOU CAN USE AN INDEX SIGNATURE TO DEFINE A FLEXIBLE OBJECT.
 */
interface Dictionary {
  [key: string]: string;
}

const translations: Dictionary = {
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
  add: (a: number, b: number): number => a + b,
  subtract(a: number, b: number): number {
    return a - b;
  },
};
console.log(`SUM: ${calculator.add(1, 2)} - SUB: ${calculator.subtract(4, 1)}`);

// 7 - EXTENDING OBJECTS
/**
 * EXTED OBJECTS USING INHERITANCE
 * IN INTERFACES.
 */
interface Animal {
  name: string;
}

interface Dog1 extends Animal {
  breed: string;
}

const dog1: Dog1 = {
  name: "Buddy",
  breed: "Pincher",
};

//  8 - INTERSECTION AND UNION TYPES
/**
 * OBJECTS CAN BE COMBINED USING INTERSECTION OR UNION TYPES.
 */
// INTERSECTION
type A = { name: string };
type B = { age: number };

type Human = A & B;

const human: Human = { name: "Eve", age: 20 };

// UNION
type Cat = { meow: () => void };
type Dog = { bark: () => void };

type Pet = Cat | Dog;

const pet: Pet = {
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
  constructor(public name: string, public age: number) {}

  gret() {
    console.log(`Hello, my name is ${this.name}`);
  }
}

const p = new Person4("Jonny", 31);
p.gret();
