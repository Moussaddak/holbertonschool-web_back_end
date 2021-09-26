// eslint-disable-line
const fs = require('fs');

function countStudents(path) {
  const cs = [];
  const swe = [];
  try {
    const data = fs.readFileSync(path, { encoding: 'utf8' });
    const lines = data.split(/\r?\n/);
    lines.forEach((line) => {
      if (line.includes('CS')) cs.push(line.split(',')[0]);
      else if (line.includes('SWE')) swe.push(line.split(',')[0]);
    });
    const totalStudents = cs.length + swe.length;
    console.log(`Number of students: ${totalStudents}`);
    console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
    console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
