// KEY UTILITIES TYPES //

// 1 - Partial<Type>
// DESCRIPTION: MAKES ALL PROPERTIES OF Type OPTIONAL.
// USE CASE: WHEN THE WORK IS WITH A SUBSET OF PROPERTIES FROM A TYPE.

interface User1 {
    id: number;
    name: string,
    age: number;
}

const partialUser: Partial<User> = { name: "Milan" };


// 2 - Required<Type>
// DESCRIPTION: MAKES ALL PROPERTIES OF type REQUIRED.
// USE CASE: ENSURES ALL OPTIONAL PROPERTIES IN A TYPE ARE FILLED.

interface User2 {
    id: number;
    name?: string;
}

const fullUser: Required<User2> = { id: 7, name: "Linsberg" };
fullUser.name = "New Name"; // CAN UPDATE


// 3 - Readonly<Type>
// DESCRIPTION: MAKES ALL PROPERTIES OF type readonly (IMMUTABLE).
// USE CASE: PREVENT UNINTENDED MODIFICATIONS.

interface User3 {
    id: number;
    name: string;
}

const readonlyUser: Readonly<User3> =  { id: 2, name: "Sintraxos" };
// Cannot assign to 'name' because it is a read-only property.ts(2540)
// ⚠ Error(TS2540)
// readonlyUser.name = "Noslarty";


// 4 - Record<Keys, Type>
// DESCRIPTION: CONSTRUCTS A TYPE WITH A SET OF PROPERTIES Keys OF TYPE Type.
// USE CASE: CREATE A MAPPED OBJECT TYPE WITH SPECIFIC KEYS AND THERI VALUE TYPE.
type Role = "admin" | "user" | "guest";

const userRoles: Record<Role, string> = {
    "admin": "FULL ACESS",
    "user": "REGULAR ACESS",
    "guest": "GUEST USER"
}


//  5 - Pick<Type, Keys>
// DESCRIPTION: CONSTRUCTS A TYPE BY PICKING A SET OF PROPERTIES "Keys" from "Type".
// USE CASE: EXTRACT A SUBSET OF PROPERTIES FROM A TYPE.
interface User4 {
    id: number;
    name: string;
    age: number;
}

type UserSummary = Pick<User4, "id" | "name">;

const summary: UserSummary = {
    id: 11,
    name: "Alfredo"
}


// 6 - Omit<Type, Keys>
// DESCRIPTION: CONSTRUCTS A TYPE BY OMITTING A SET OS PROPERTIES Keys from type.
// USE CASE: REMOVE SPECIFIC PROPERTIES FROM A TYPE.
interface UserOmit {
    id: number;
    name: string;
    age: number;
}

type UserWithoutAge = Omit<UserOmit, "age">;

const userWithoutAge: UserWithoutAge = {
    id: 275,
    name: "Proskhanlò"
}


// 7 - Exclude<Type, ExcludedUnion>
// DESCRIPTION: CONSTRUCTS A TYPE BY EXCLUDING MEMBERS OF ExcludedUnion FROM Type
// USE CASE: FILTER OUT SPECIFIC VALUES FROM A UNION.

type l9_Status = "active" | "inactive" | "archived";

type ActiveStatus = Exclude<l9_Status, "archived">;


// 8 - Extract<Type, IncludedUnion>
// DESCRIPTION: CONSTRUCTS A TYPE BY EXTRACTING MEMBERS OF IncludedUnion FROM Type.
// USE CASE: NARROW DOWN A UNION TYPE.

type l9_Status2 = "active" | "inactive" | "archived";

type ArchivedStatus = Extract<l9_Status2, "archived">;

// 9 - NonNullable<Type>
// DESCRIPTION: CONSTRUCTS A TYPE BY EXCLUDING "null" and "indefined" FROM "Type".
// USE CASE: ENSURE A TYPE DOESN´T INCLUDE "null" OR "undefined".

type Input = string | null | undefined;

type ValidInput = NonNullable<Input>;


// 10 - ReturnType<Type>
// DESCRIPTION: CONSTRUCTS A TYPE CONSISTING OF THE RETURN TYPE OF FUNCTION "Type".
// USE CASE: INFER THE RETURN TYPE OF A FUNCTION.
let getUser = () => {
    return { id: 94, name: "Nishlas", age: 22 };
}
type userReturnType = ReturnType< typeof getUser >;


// 11 - InstanceType<Type>
// DESCRIPTION: CONSTRUCTS A TYPE CONSISTING OF THE INSTANCE TYPE OF A CONSTRUCTOR FUNCTION.
class Programmer {
    id: number;
    name: string;

    constructor (id: number, name: string) {
        this.id = id;
        this.name = name;
    }
}

type programmerType = InstanceType< typeof Programmer >;


// COMBINING UTILITY TYPES
// UTILITY TYPES CAN BE COMBINED TO CREATE POWERFUL TRANSFORMATIONS

type PartialReadonly<T> = Readonly<Partial<T>>;

interface l9_User {
    id: number;
    name: string;
    age: number;
}

const l9_user: PartialReadonly<l9_User> = {
    name: "IMMUTABLE NAME"
};

// Cannot assign to 'name' because it is a read-only property.ts(2540)
// ⚠ Error(TS2540)
// l9_user.name = "NEW NAME";