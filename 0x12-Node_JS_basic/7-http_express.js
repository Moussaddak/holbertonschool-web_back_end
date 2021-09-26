const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', (req, res) => {
  countStudents(process.argv[2]).then((response) => {
    res.send(`This is the list of our students\n${response.join('\n')}`);
  }).catch((error) => {
    res.send(`This is the list of our students\n${error.message}`);
  });
});
const port = 1245;
app.listen(port);
module.exports = app;
