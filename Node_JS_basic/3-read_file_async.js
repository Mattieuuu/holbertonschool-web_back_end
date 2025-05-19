const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data
      .toString()
      .split('\n')
      .filter((line) => line.trim().length > 0);
    
    const students = lines.slice(1);
    console.log(`Number of students: ${students.length}`);

    const studentsByField = {};
    students.forEach((student) => {
      const [firstName, , , field] = student.split(',');
      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstName);
    });

    Object.keys(studentsByField).forEach((field) => {
      console.log(
        `Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}`
      );
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
