// ENUMS

// 1 - NUMERIC ENUMS
/**
 * NUMERIC ENUMS ARE THE DEFAULT TYPE. EACH MEMBER OS A NUMERIC ENUM
 * IS ASSGNED A NUMBER, STARTING FROM 0 BY DEFAULT, OR A SPECIFIED STARTING VALUE.
 */
enum Direction {
  Up, // 0
  Down, // 1
  Left, // 2
  Right, // 3
}

console.log(Direction.Up); // OUTPUT: 0
console.log(Direction.Right); // OUTPUT: 3
console.log(Direction[2]); // OUTPUT: "Left" (REVERSE MAPPING)

// CUSTOM STARTING VALUES
/**
 * IS POSSIBLE TO SET THE STARTING VALUE OF THE ENUM, AND THE REST WILL INCREMENT
 * AUTOMATICALLY
 */

enum Direction2 {
  Up = 0,
  Down,
  Left,
  Right,
}

console.log(Direction2.Down); // OUTPUT: 1

// 2 - STRING ENUMS
/**
 * STRING ENUMS ASSIGN STRING VALUES TO THE MEMBER INSTEAD OF NUMERIC
 * VALUES. THEY DON´T SUPPORT REVERSE MAPPING LIKE NUMERIC ENUMS.
 */
enum Color {
  Red = "RED",
  Green = "GREEN",
  Blue = "BLUE",
}

console.log(Color.Red);
console.log(Color.Green);

// 3 - HETEROGENEOUS ENUMS
/**
 * ENUMS CAN MIX STRINGS AND NUMERIC MEMBERS, THOUGH THIS IS GENERALLY
 * NOT RECOMMENDEDAS IT CAN LEAD TO CONFUSION.
 */
enum Mix {
  Yes = "YES",
  No = 0,
}

console.log(Mix.Yes); // OUTPUT: "YES"
console.log(Mix.No); // OUTPUT: 0

// 4 - ENUM AS A TYPE
/**
 * ENUMS CAN ALSO ACT AS TYPES FOR VARIABLES
 * OR FUNCTION PARAMETERS.
 */
enum Status {
    Active,
    Inactive,
    Pending
}

function getStatus(status: Status): string {
    switch (status) {
        case Status.Active:
            return "THE STATUS IS ACTIVE!";
        case Status.Inactive:
            return "THE STATUS IS INACTIVE!";
        case Status.Pending:
            return "THE STATUS IS PENDUNG!";
    }
}

console.log(getStatus(Status.Active)); // OUTPUT: "THE STATUS IS ACTIVE"


// 5 - COMPUTED AND CONSTANT MEMBERS
/**
 * ENUMS CAN HAVE VALUES (EVALUATED AT COMPILE-TIME) OR
 * COMPUTED VALUE (EVALUATED AT RUNTIME).
 */
// CONSTANT MEMBERS: THESE ARE EVALUATED AT COMPILE-TIME AND ARE SIMPLE EXPRESSIONS.
enum ConstantEnum {
    A = 10,
    B = A * 2 // 20
}

// COMPUTED MEMBERS: THESE REQUIRE RUNTIME EVALUATION.
const baseValue = 5;

enum ComputedEnum {
    A = baseValue + 3, // 8
    B = Math.random() * 10, // COMPUTED AT RUNTIME
}

// 6 - REVERSE MAPPING (NUMERIC ENUMS)
/**
 * NUMERIC ENUMS SUPPORT REVERSE MAPPING, WHICH ALLOWS YOU TO ACESS
 * THE NAME OF A MEMBER USING ITS VALUE. (IS NOT AVAILABLE FOR STRINGS ENUMS)
 */
enum Days {
    Sunday = 0,
    Monday = 1
}

console.log(Days[0]); // OUTPUT: "Sunday"
console.log(Days[1]); // OUTPUT: "Monday"


// 7 - DECLARING ENUM WITH CONST
/**
 * USING CONST ENUM CAM IMPROVE PERFORMANCE AND REDUCE
 * THE GENERATED JS CODE BY INLINING THE ENUM VALUES.
 * 
 * WITH "const enum", NO OBJECT IS CREATED IN THE OUTPUT JS,
 * AND THE VALUES ARE DIRECTLY INLINED.
 */
const enum TrafficLight {
    Red,
    Yellow,
    Green
}

const signal: TrafficLight = TrafficLight.Red;
console.log(signal);

// 8 - AMBIENTE ENUMS
/**
 * AMBIENTE ENUMS ARE USED TO DESCRIBE ENUMS
 * DEFINED ELSEWHERE (e.g., IN A LIBRARY).
 * 
 * "declare" KEYWORD TO DEFINE THEM.
 */

declare enum ExternalEnum {
    X = 1,
    Y,
    Z
}


// ROLE EXAMPLE
enum UserRole {
    Admin = "ADMIN",
    User = "USER",
    Guest = "GUEST"
}

function checkAcess(role: UserRole) {
    if (role === UserRole.Admin){
        console.log("ACESS GRANTED TO ADMIN!");
    } else {
        console.log("ACESS RESTRICTED!");
    }
}

checkAcess(UserRole.User); // OUTPUT: "ACESS RESTRICTED!"


// ADVANTAGES OF ENUMS
/**
 * READABILITY: REPLACING MAGIC NUMBERS OR STRINGS WOTH MEANINGFUL NAMES.
 * TYPE SAFETY: PREVENTS INVALID VALUES FROM BEING ASSIGNED.
 * REVERSE MAPPING: NUMERIC ENUMS ALLOW BIDIRECTIONAL LOOKUP.
 */

// COMMON USE CASES
/**
 * 1. REPRESENTING FIXED CATEGORIES: DAYS OF THE WEEK, DIRECTIONS, COLORS,
 * STATES, ETC.
 * 2. IMPROVING CODE MAINTAINABILITY: AVOID USING HARDCODED STRINGS OR
 * NUMBERS.
 */