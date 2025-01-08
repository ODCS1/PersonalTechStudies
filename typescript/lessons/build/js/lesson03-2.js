"use strict";
// ENUMS
// 1 - NUMERIC ENUMS
/**
 * NUMERIC ENUMS ARE THE DEFAULT TYPE. EACH MEMBER OS A NUMERIC ENUM
 * IS ASSGNED A NUMBER, STARTING FROM 0 BY DEFAULT, OR A SPECIFIED STARTING VALUE.
 */
var Direction;
(function (Direction) {
    Direction[Direction["Up"] = 0] = "Up";
    Direction[Direction["Down"] = 1] = "Down";
    Direction[Direction["Left"] = 2] = "Left";
    Direction[Direction["Right"] = 3] = "Right";
})(Direction || (Direction = {}));
console.log(Direction.Up); // OUTPUT: 0
console.log(Direction.Right); // OUTPUT: 3
console.log(Direction[2]); // OUTPUT: "Left" (REVERSE MAPPING)
// CUSTOM STARTING VALUES
/**
 * IS POSSIBLE TO SET THE STARTING VALUE OF THE ENUM, AND THE REST WILL INCREMENT
 * AUTOMATICALLY
 */
var Direction2;
(function (Direction2) {
    Direction2[Direction2["Up"] = 0] = "Up";
    Direction2[Direction2["Down"] = 1] = "Down";
    Direction2[Direction2["Left"] = 2] = "Left";
    Direction2[Direction2["Right"] = 3] = "Right";
})(Direction2 || (Direction2 = {}));
console.log(Direction2.Down); // OUTPUT: 1
// 2 - STRING ENUMS
/**
 * STRING ENUMS ASSIGN STRING VALUES TO THE MEMBER INSTEAD OF NUMERIC
 * VALUES. THEY DON´T SUPPORT REVERSE MAPPING LIKE NUMERIC ENUMS.
 */
var Color;
(function (Color) {
    Color["Red"] = "RED";
    Color["Green"] = "GREEN";
    Color["Blue"] = "BLUE";
})(Color || (Color = {}));
console.log(Color.Red);
console.log(Color.Green);
// 3 - HETEROGENEOUS ENUMS
/**
 * ENUMS CAN MIX STRINGS AND NUMERIC MEMBERS, THOUGH THIS IS GENERALLY
 * NOT RECOMMENDEDAS IT CAN LEAD TO CONFUSION.
 */
var Mix;
(function (Mix) {
    Mix["Yes"] = "YES";
    Mix[Mix["No"] = 0] = "No";
})(Mix || (Mix = {}));
console.log(Mix.Yes); // OUTPUT: "YES"
console.log(Mix.No); // OUTPUT: 0
// 4 - ENUM AS A TYPE
/**
 * ENUMS CAN ALSO ACT AS TYPES FOR VARIABLES
 * OR FUNCTION PARAMETERS.
 */
var Status;
(function (Status) {
    Status[Status["Active"] = 0] = "Active";
    Status[Status["Inactive"] = 1] = "Inactive";
    Status[Status["Pending"] = 2] = "Pending";
})(Status || (Status = {}));
function getStatus(status) {
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
var ConstantEnum;
(function (ConstantEnum) {
    ConstantEnum[ConstantEnum["A"] = 10] = "A";
    ConstantEnum[ConstantEnum["B"] = 20] = "B"; // 20
})(ConstantEnum || (ConstantEnum = {}));
// COMPUTED MEMBERS: THESE REQUIRE RUNTIME EVALUATION.
const baseValue = 5;
var ComputedEnum;
(function (ComputedEnum) {
    ComputedEnum[ComputedEnum["A"] = 8] = "A";
    ComputedEnum[ComputedEnum["B"] = Math.random() * 10] = "B";
})(ComputedEnum || (ComputedEnum = {}));
// 6 - REVERSE MAPPING (NUMERIC ENUMS)
/**
 * NUMERIC ENUMS SUPPORT REVERSE MAPPING, WHICH ALLOWS YOU TO ACESS
 * THE NAME OF A MEMBER USING ITS VALUE. (IS NOT AVAILABLE FOR STRINGS ENUMS)
 */
var Days;
(function (Days) {
    Days[Days["Sunday"] = 0] = "Sunday";
    Days[Days["Monday"] = 1] = "Monday";
})(Days || (Days = {}));
console.log(Days[0]); // OUTPUT: "Sunday"
console.log(Days[1]); // OUTPUT: "Monday"
const signal = 0 /* TrafficLight.Red */;
console.log(signal);
// ROLE EXAMPLE
var UserRole;
(function (UserRole) {
    UserRole["Admin"] = "ADMIN";
    UserRole["User"] = "USER";
    UserRole["Guest"] = "GUEST";
})(UserRole || (UserRole = {}));
function checkAcess(role) {
    if (role === UserRole.Admin) {
        console.log("ACESS GRANTED TO ADMIN!");
    }
    else {
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
