// Import des modules nécessaires
const http = require('http'); // Module pour créer un serveur HTTP
const fs = require('fs').promises; // Module pour les opérations fichiers asynchrones

/**
 * Fonction asynchrone qui compte et organise les étudiants par field
 * @param {string} path - Chemin vers le fichier CSV
 * @returns {string} - Chaîne formatée avec les statistiques des étudiants
 */
async function countStudents(path) {
  try {
    // Lecture asynchrone du fichier CSV
    const data = await fs.readFile(path, 'utf8');
    
    // Traitement du fichier : séparation en lignes et suppression des lignes vides
    const lines = data.toString().split('\n').filter(line => line.trim().length > 0);
    
    // Suppression de l'en-tête et récupération des données étudiants
    const students = lines.slice(1);
    let output = `Number of students: ${students.length}\n`;

    // Objet pour stocker les étudiants par field
    const studentsByField = {};
    
    // Parcours de chaque étudiant pour les organiser par field
    students.forEach(student => {
      // Extraction du prénom et du field (les ,, ignorent lastname et age)
      const [firstName, , , field] = student.split(',');
      // Création du tableau pour le field s'il n'existe pas
      if (!studentsByField[field]) studentsByField[field] = [];
      // Ajout de l'étudiant dans son field
      studentsByField[field].push(firstName);
    });

    // Construction de la chaîne de sortie pour chaque field
    Object.keys(studentsByField).forEach(field => {
      output += `Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}\n`;
    });
    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

// Création du serveur HTTP
const app = http.createServer(async (req, res) => {
  // Configuration de l'en-tête de réponse en texte brut
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  
  // Gestion des routes
  if (req.url === '/') {
    // Route racine : affiche un message d'accueil
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    // Route /students : affiche les statistiques des étudiants
    try {
      const output = await countStudents(process.argv[2]);
      res.end(`This is the list of our students\n${output}`);
    } catch (error) {
      res.end('This is the list of our students\nCannot load the database');
    }
  }
});

// Démarrage du serveur sur le port 1245
app.listen(1245);

// Export du serveur pour les tests
module.exports = app;
