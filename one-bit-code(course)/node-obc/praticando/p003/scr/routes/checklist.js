const express = require('express');
const router = express.Router();

router.get('/checklist', (req,res) => {
    console.log("Check List!");
    res.send();
});

module.exports = router;