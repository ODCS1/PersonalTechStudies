const http = require('http')

const server = http.createServer(
    (req,res) => {
        console.log(req.url)
        console.log(req.method)
        res.statusCode = 200
        res.end('<h1>SITE NO AR/h1>')
    }
)

server.listen(3000, () => {
    console.log("Server no ar.")
})