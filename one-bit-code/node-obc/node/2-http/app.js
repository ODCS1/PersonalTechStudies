const http = require("http")

http.createServer(
    (req,res) => {
        res.end("<h1>HTTP</h1>")
    }
).listen(3000, () => {
    console.log("Servidor ON, na porta 3000.")
})