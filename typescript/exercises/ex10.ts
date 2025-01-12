// Exercise 10: Object Types
// Objective: Create and manipulate objects using type annotations.

let book: { title: string, author: string, releaseDate: string } =  {
    title: "The book",
    author: "Ricardo Feltre",
    releaseDate: "2004"
}

console.log(`Title: ${book.title}, Author: ${book.author} and Release Date: ${book.releaseDate}.`)

book.title = "Reformulated Book";
// book.releaseDate = 2006; // ERROR TYPE