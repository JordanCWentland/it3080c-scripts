const express = require("express");
const morg = require("morgan");
const path = require("path");
var dev = express();

dev.use(morg('test'));

dev.use(express.static(path.join(__dirname, 'content')));

dev.get('*', function(req, res) {
   res.send('oh');
});

dev.listen(8000);
console.log("web server started on port 8000");

