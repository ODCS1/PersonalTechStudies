// import React from "react"; // ADDED IN babel.config.js
import ReactDOM from "react-dom/client";
import { App } from "./App";
// import { App } from "./App";

// BEFORE REACT 18
// render(<h1>Hello, World!</h1>, document.getElementById("root"));

// THIS IS CONCURRENT RENDERING IN REACT 18.
const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<App />);
