"use strict";
// KEY UTILITIES TYPES //
const partialUser = { name: "Milan" };
const fullUser = { id: 7, name: "Linsberg" };
fullUser.name = "New Name"; // CAN UPDATE
const readonlyUser = { id: 2, name: "Sintraxos" };
const userRoles = {
    "admin": "FULL ACESS",
    "user": "REGULAR ACESS",
    "guest": "GUEST USER"
};
const summary = {
    id: 11,
    name: "Alfredo"
};
const userWithoutAge = {
    id: 275,
    name: "Proskhanlò"
};
// 10 - ReturnType<Type>
// DESCRIPTION: CONSTRUCTS A TYPE CONSISTING OF THE RETURN TYPE OF FUNCTION "Type".
// USE CASE: INFER THE RETURN TYPE OF A FUNCTION.
let getUser = () => {
    return { id: 94, name: "Nishlas", age: 22 };
};
// 11 - InstanceType<Type>
// DESCRIPTION: CONSTRUCTS A TYPE CONSISTING OF THE INSTANCE TYPE OF A CONSTRUCTOR FUNCTION.
class Programmer {
    constructor(id, name) {
        this.id = id;
        this.name = name;
    }
}
const l9_user = {
    name: "IMMUTABLE NAME"
};
// Cannot assign to 'name' because it is a read-only property.ts(2540)
// ⚠ Error(TS2540)
// l9_user.name = "NEW NAME";
