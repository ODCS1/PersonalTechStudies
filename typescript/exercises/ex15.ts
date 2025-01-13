// Exercise 15: Null and Undefined
// Objective: Understand how TypeScript handles null and undefined.

interface Paper {
  size: string;
  color: string;
  manufacturer?: string;
}

let paper: Paper = {
  size: "210mmx297mm",
  color: "white",
};
console.log(paper.manufacturer); // undefined

let paper2: NonNullable<Paper> = {
  size: "210mmx297mm",
  color: "blue",
  manufacturer: "Some producer",
};

const user = {
  profile: {
    name: "",
    age: 36,
  },
};

console.log(user.profile?.name);

// Property 'height' does not exist on type '{ name: string; age: number; }'.ts(2339)
// ⚠ Error (TS2339)  |
// Property height does not exist on type
// console.log(user.profile?.height); // ERROR

// EQUALITY CHECKS
console.log(undefined == null); // true
console.log(undefined === null); // false

let value: string | undefined | null;
let result = value ?? "DEFAULT";
console.log(`RESULT: ${result}`);

type NullableString = string | undefined | null;
type NonNullableString = NonNullable<NullableString>;
let hand: NonNullableString = "Fingers;";
// Type 'undefined' is not assignable to type 'string'.ts(2322)
// hand = null;
// hand = undefined;
