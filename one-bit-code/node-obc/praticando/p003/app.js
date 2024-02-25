const express = require('express');
const checkListRouter = require("./scr/routes/checklist");

const app = express();

app.use(checkListRouter);

app.listen(3000, () => {
    console.log("Porta 3000.")
})
