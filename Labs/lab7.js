const http = require('http');
const os = require("os");
const ip = require("ip");
const fs = require("fs");
const port = 3000;

http.createServer((req, res) => {
	if (req.url === "/") {
		fs.readFile("./public/index.html", "UTF-8", (err, body) => {
			res.writeHead(200, {
				"Content-Type": "text/html"
			});
			res.end(body);
		});
	} else if (req.url.match("/sysinfo")) {
		//variables
		var hostname = os.hostname();
		var ipAddr = ip.address();
		var totalmem = Number((os.totalmem() / 1000000).toPrecision(7));
		var freemem = Number((os.freemem() / 1000000).toPrecision(7));
		var numcpu = os.cpus().length;
		//uptime math 
		var upSec = os.uptime();
		var upMin = upSec / 60;
		var upHour = upMin / 60;
		var upDay = upHour / 24;
		upSec = Math.floor(upSec)
		upMin = Math.floor(upMin)
		upHour = Math.floor(upHour)
		upDay = Math.floor(upDay)
		upDay = upDay % 60
		upHour = upHour % 60
		upMin = upMin % 60
		upSec = upSec % 60
		var uptime = ` ${upDay} Days, ${upHour} Hours, ${upMin} Minutes, ${upSec} Seconds `
		html = `
      <!DOCTYPE html>
      <html>
        <head>
          <title>Node JS Response</title>
        </head>
        <body>
          <p>Hostname: ${hostname}</p>
          <p>IP: ${ipAddr}</p>
          <p>Server Uptime: ${uptime} </p>
          <p>Total Memory: ${totalmem} MB</p>
          <p>Free Memory: ${freemem} MB</p>
          <p>Number of CPUs: ${numcpu} </p>
        </body>
      </html>`
		res.writeHead(200, {
			"Content-Type": "text/html"
		});
		res.end(html);
	} else {
		res.writeHead(404, {
			"Content-Type": "text/plain"
		});
		res.end(`404 File Not Found at ${req.url}`);
	}
}).listen(port);

console.log("Server listening on port 3000");