// 1 - NULLISH COALESCING OPERATOR

const age0 = 0;

// 0, "", [], false, undefined, null => false;

// console.log("AGE: " + (age || "Not valid!")); // false
console.log("AGE: " + (age0 ?? "Not Valid!"));


// 2 - Objects
const user = {
  name: "Gyóstrask",
  age: 27,
  address: {
    street: "T address",
    number: 35
  },
};


console.log("name" in user);
console.log(Object.keys(user));
console.log(Object.values(user));
console.log(Object.entries(user));

// DESTRUCTURING
const { address, age: yo, nickname = "user" } = user;
console.log({address, yo, nickname})


function getAge({ age }) {
  return age;
}

console.log(getAge(user));

// REST OPERATOR
const { name, ...rest } = user;
console.log(rest)