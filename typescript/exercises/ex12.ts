// Exercise 14: String Literal Types
// Objective: Use string literal types to restrict variable values.

type Role = "Admin" | "User" | "Guest" | "Client";

function verifyTypeRole(role: Role):boolean {

    return role === "Admin"
        ? true
        : false;
}

console.log(verifyTypeRole("Guest"));
