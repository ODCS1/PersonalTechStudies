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
    number: 35,
    zip: {
      code: "45629000",
      city: "Intrósnk",
    },
    showFullAdress() {
      return "ok";
    },
  },
};

console.log("name" in user);
console.log(Object.keys(user));
console.log(Object.values(user));
console.log(Object.entries(user));

// DESTRUCTURING
const { address, age: yo, nickname = "user" } = user;
console.log({ address, yo, nickname });

function getAge({ age }) {
  return age;
}

console.log(getAge(user));

// REST OPERATOR
const { name, ...rest0 } = user;
console.log(rest0);

const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const [first, , third, ...rest] = array;
console.log({ first, third, ...rest });

// SHORT SYNTAX
const name2 = "Distórstik";
const age2 = 27;

const user2 = {
  name2,
  age2,
};

// OPTIONAL CHAINING
const code = user.address
  ? user.address.zip
    ? user.address.zip.code
    : "Not Found!"
  : "Not Found";

console.log(user.address?.zip?.code ?? "Not Found!");
console.log(user.address?.showFullAdress?.() ?? "Not Found!");

const key = "state";
console.log(user.address?.[key]);

// 3 - ARRAY METHODS
const array2 = [1, 2, 3, 4, 5];

let output = "";
for (const i of array2) {
  output += i;
}
console.log(output);

output = "";
array2.forEach((item) => {
  output += item;
});
console.log(output);

// FOREACH X MAP
let novoArray = [];
array2.forEach((item) => {
  novoArray.push(item * 2);
});

console.log(novoArray);
novoArray = [];
novoArray = array2.map((item) => {
  return item * 2;
});
console.log(novoArray);


// FILTER
const newArray = array2
  .filter(item => item % 2 === 0)
  .map(item => item * 10);

console.log(newArray);

// EVERY
console.log(array2.every(item => typeof item === "number"));

// SOME
console.log(array2.some(item => typeof array2 === "string"));

//  FIND
console.log(array2.find(item => item % 2 === 0));

// FIND INDEX
console.log(array2.findIndex(item => item === 4)) // RETURN -1 IF DON´T FIND

// REDUCE
const sumReduce = array2.reduce((prev, current) => prev + current, 0);
console.log(sumReduce);


// TEMPLATE LITERALS
const newName = null;
const message = `Welcome, ${newName ?? "Visitor"}!`;
console.log(message);


// PROMISES
const sumTwoNumbers = (a, b) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => { // TO SEE THE TIME TO RETURN THE VALUE
      resolve(a + b);
    }, 2000);
  });
}

sumTwoNumbers(1,3)
  .then(sumValue => {
    console.log(sumValue);
  })
  .catch (err => {
    console.log(err);
  });


fetch("https://api.github.com/users/ODCS1")
  .then(response => {
    return response.json();
  })
  .then(body => {
    console.log(body);
  })
  // .then(response => {
  //   response.json().then(body => {
  //     console.log(body);
  //   })
  // })
  .catch(err => {
    console.log(err);
  })
  .finally(() => {
    console.log("FINALLY");
  }
);


async function getDataGitHub() {
  try {
    const response = await fetch("https://api.github.com/users/ODCS1");
    const body = await response.json();
  
    console.log(body);
    return body.name;
  } catch(err) {
    console.log(err);
  } finally {
    console.log("FINALLY2")
  }
}

getDataGitHub().then(name => {
  console.log(name);
});

//  IMPORTS
import { sum, sub as newSub } from "./lib/math";

console.log("SUM: " + sum(1, 4));
console.log("NEW SUB: ", newSub(9, 5));


import * as math from "./lib/math"
console.log("SUB: " + math.sub(4,1));

import { sum as sum2 } from "./lib/sum";
console.log("SUM FILE: " + sum2(7, 3));