// Exercise 6: Type Inference
// Objective: Observe how TypeScript infers types based on the assigned values.

let pi = 3.14;
const enum Data {
    January = "01",
    February = "02",
    March = "03",
    Aril = "04",
    May = "05",
    June = "06",
    July = "07",
    August = "08",
    September = "09",
    October = "10",
    November = "11",
    December = "12"
}

type mixDataType = (string | number)[] | undefined | null;
type stringOrNumber = string | number;
type typeTest = string | never | string[]


let myObjTest = {
    "id": 1,
    "notation": "n1"
}

interface Language {
    origin: string,
    speakers: number;
}

let objSpanish:Language = {
    origin: "Spain",
    speakers: 8000000000
}