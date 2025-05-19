const fs = require('fs');

function countStudents(path) {
  try {
    // Lire le fichier
    const data = fs.readFileSync(path, 'utf8');
    
    // Séparer les lignes et enlever les lignes vides
    const lines = data.toString().split('\n').filter(Boolean);
    
    // Enlever l'en-tête et garder que les étudiants
    const students = lines.slice(1);
    
    // Afficher le nombre total d'étudiants
    console.log(`Number of students: ${students.length}`);
    
    // Organiser les étudiants par field
    const studentsByField = {};
    students.forEach((student) => {
      const [firstName, , , field] = student.split(',');
      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstName);
    });
    
    // Afficher les résultats pour chaque field
    Object.keys(studentsByField).forEach((field) => {
      console.log(
        `Number of students in ${field}: ${studentsByField[field].length}. ` +
        `List: ${studentsByField[field].join(', ')}`
      );
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
