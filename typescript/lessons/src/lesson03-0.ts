let l3_stringArr: string[] = ["one", "two", "hey"];

let l3_guitars = ["Strat", "Les Paul", 5150];

let l3_mixedData = ["EVH", 1954, true];

l3_stringArr[0] = "five";
l3_stringArr.push("hi");

l3_guitars[0] = 1950;
l3_guitars.unshift("new");

//  ANY TYPE
let l3_test = [];

// TUPLE
let l3_data: [string, number, number] = ["User", 37, 82.7];

const l3_student = ["Doug", "Computer Science", "4 Semester", "45734"];

let l3_person: [string, number];
l3_person = ["John", 30]; // ✅ VALID
// l3_person = [30, "John"]; // ❌ ERROR: ORDER IS INCORRECT
// l3_person = ["John", 30, true]; // ❌ ERROR: TOO MANY ELEMENTS

/**
 * BY DEFAULT, TUPLES I TYPESCRIPT ARE MUTABLE
 * MEANING IS POSSIBLE MODIFY THEI ELEMENTS OR
 * EVEN ADD NEW ONES. TO MAKE TUPLES IMMUTABLE
 * IS ONLY USE "readonly" KEYWORD
 */
// RGB COLOR
const l3_color: readonly [number, number, number] = [231, 156, 67];
// (COMPILER) -> Property 'push' does not exist on type 'readonly [number, number, number]'.ts(2339) any
// l3_color.push()

// NAMED TUPLES
/**
 * NAMED TUPLES ARE CREATED BY ASSIGNING NAMES TO EACH ELEMENT
 * WITHIN THE TYPE DECLARATION.
 */
type l3_Coordinate = [x: number, y: number, z: number];
const l3_point3D: l3_Coordinate = [3, 10, 52];

// ACCESSING ELEMENTS
const l3_XCoordinate: number = l3_point3D[0];

// OBJECTS
let l3_myObj: object;
l3_myObj = [];
console.log(typeof l3_myObj);
l3_myObj = {};

const exampleObj = {
  prop1: "Dave",
  prop2: true,
};

exampleObj.prop1 = "Aston";

type l3_Guitarist = {
  name: string;
  active?: boolean;
  albums: (string | number)[];
};

let jp: l3_Guitarist = {
  name: "Jimmy",
  albums: ["I", "II", "IV"],
};

const greetGuitarist = (guitarist: l3_Guitarist) => {
    return `Name: ${guitarist.name}`;
};


console.log(greetGuitarist(jp));