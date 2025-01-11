// Exercise 4: Classes and Inheritance
// Objective: Create a class Employee that extends a base class Person.

class Person {
    id: number;
    name: string;

    constructor(id: number, name: string) {
        this.id = id;
        this.name = name;
    }

    public get getName():string {
        return this.name;
    }
}


class Employee extends Person {
    jobTitle: string;

    constructor(id: number, name: string, jobTitle: string){
        super(id, name);
        this.jobTitle = jobTitle;
    }

    public get allData() {
        return `Id: ${this.id} \nName: ${this.name} \nJob Title: ${this.jobTitle}` 
    }
}


let employee = new Employee(1 ,"Markris", "developer");
console.log(employee.allData);