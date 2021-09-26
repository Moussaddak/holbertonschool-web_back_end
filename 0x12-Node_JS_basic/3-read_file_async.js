// eslint-disable-line
const fs = require('fs');

function countStudents(path) {
  const cs = [];
  const swe = [];
  const Response = [];

  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      const lines = data.split(/\r?\n/);
      lines.forEach((line) => {
        if (line.includes('CS')) cs.push(line.split(',')[0]);
        else if (line.includes('SWE')) swe.push(line.split(',')[0]);
      });
      const totalStudents = cs.length + swe.length;
      Response.push(`Number of students: ${totalStudents}`);
      Response.push(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
      Response.push(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
      console.log(`Number of students: ${totalStudents}`);
      console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
      console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
      resolve(Response);
    });
  });
}

module.exports = countStudents;
