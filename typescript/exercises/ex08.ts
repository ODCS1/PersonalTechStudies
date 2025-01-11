// Exercise 8: Utility Types
// Objective: Use some of TypeScript’s built-in utility types.

interface Computer {
    ram: number;
    motherboard: string;
    cpu: string;
    gpu: string;
    isAirCooler: boolean;
}

let computer1: Partial<Computer> = {
    ram: 16,
    motherboard: "b550m aorus elite",
    cpu: "Ryzen 5700g",
    isAirCooler: false
}

let computer2: Required<Computer> = {
    ram: 32,
    motherboard: "A620 Asus TUF gaming",
    cpu: "Ryzen 5 8500g",
    gpu: "rtx 4070",
    isAirCooler: false
}

interface Admin {
    id: number;
    acess: string;
    name: string;
    jobTitle: string;
}

let admin: Required<Admin> = {
    id: 8,
    acess: "total",
    name: "Rotróstivk",
    jobTitle: "TechLead"
}

type role = "user" | "admin" | "guest";

let userRoles: Record<role, string> = {
    admin: "ADMIN",
    user: "USER",
    guest: "GUEST"
}