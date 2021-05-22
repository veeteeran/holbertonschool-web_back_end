const http = require('http');
const countStudents = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  const { method, url } = req;
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (method === 'GET') {
    if (url === '/') {
      res.end('Hello Holberton School!');
    } else if (url === '/students') {
      await countStudents(process.argv[2])
        .then((value) => {
          res.write('This is the list of our students\n');
          res.write(`Number of students: ${value.lines.length}\n`);
          res.write(`Number of students in CS: ${value.cs.length}. List: ${value.cs.join(', ')}\n`);
          res.write(`Number of students in SWE: ${value.swe.length}. List: ${value.swe.join(', ')}`);
        })
        .catch(console.error);
      res.end();
    }
  }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
