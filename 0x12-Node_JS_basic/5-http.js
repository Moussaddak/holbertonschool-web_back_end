const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  if (req.url === '/') res.end('Hello Holberton School!');
  else if (req.url === '/students') {
    await countStudents(process.argv[2])
      .then((success) => {
        const output = `This is the list of our students\n${success}`;
        res.end(output);
      })
      .catch((err) => {
        const output = `This is the list of our students\n${err.message}`;
        res.end(output);
      });
  }
});

app.listen(port);

module.exports = app;
