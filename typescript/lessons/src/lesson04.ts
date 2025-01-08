// TYPE ALIASES
type stringOrNumber = string | number;

type stringOrNumberArray = (string | number)[];

type l4_Guitarist = {
  name: string;
  active?: boolean;
  albums: stringOrNumberArray;
};

type UserId = stringOrNumber;

// LITERAL TYPES
let myName: "Dave";

let userName: "Dave" | "John" | "Amy";
userName = "Amy";

// FUNCTIONS
const add = (a: number, b: number): number => {
    return a + b;
}

const logMsg = (message: any): void => {
    console.log(message);
}

logMsg("Hello!");
logMsg(add(2, 3));

let subtract = function (c: number, d: number): number {
    return c - d;
}

type mathFunction = (a: number, b: number) => number
// interface mathFunction {
//     (a: number, b: number): number;
// }

let multiply: mathFunction = function (c, d) {
    return c * d;
}

logMsg(multiply(2, 2));

// OPTIONAL PARAMETES
const addAll = (a: number, b: number, c?: number): number => {
    if (typeof c !== "undefined"){
        return a + b + c;
    }
    return a + b;
}

// DEFAULT PARAM VALUE
const sumAll = (a: number = 10, b: number, c: number = 2): number => {
    return a + b + c;
}

logMsg(addAll(2, 3, 2))
logMsg(addAll(2, 3))
logMsg(sumAll(2, 3))
logMsg(sumAll(undefined, 3))


// REST PARAMETERS
let total = function(a: number, ...nums: number[]): number {
    return nums.reduce((total, num) => total + num, a);
}
logMsg(total(10, 2, 3));

const createError = (errMsg: string): never => {
    throw new Error(errMsg);
}

const infinite = () => {
    let i: number = 1;
    while (true) {
        i++;
        // if (i == 5) break; // void
    }
}


// CUSTOM TYPE GUARD
const isNumber = (value: any): boolean => {
    return typeof value === "number"
        ? true
        : false;
}

// USE OF THE NEVER TYPE
const numberOrString = (value: number | string): string => {
    if (typeof value === "string") return "string";
    if (typeof value === "number") return "number";
    return createError("THIS SHOULD NEVER HAPPEN!");
}