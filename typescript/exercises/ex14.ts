// Exercise 14: For Loop with TypeScript Arrays
// Objective: Practice iterating through arrays using a for loop.


let fruits: string[] = ["melon", "orange", "strawberry", "banana"];


for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

for (let p in fruits) {
    console.log(p);
}

for (let fruit of fruits) {
    console.log(fruit);
}