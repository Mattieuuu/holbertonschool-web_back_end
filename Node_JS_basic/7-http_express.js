// Importation des modules nécessaires
const express = require('express'); // Framework web pour Node.js
const fs = require('fs').promises; // Module pour les opérations de fichiers asynchrones

/**
 * Fonction asynchrone qui analyse un fichier CSV d'étudiants
 * @param {string} path - Chemin vers le fichier CSV
 * @returns {string} - Texte formaté avec les statistiques des étudiants
 */
async function countStudents(path) {
  try {
    // Lecture asynchrone du fichier CSV
    // 'utf8' spécifie l'encodage du fichier
    const data = await fs.readFile(path, 'utf8');

    // Transformation du contenu du fichier :
    // 1. Conversion en chaîne de caractères
    // 2. Séparation en lignes
    // 3. Suppression des lignes vides
    const lines = data
      .toString()
      .split('\n')
      .filter(line => line.trim().length > 0);

    // Suppression de la ligne d'en-tête et récupération des données
    const students = lines.slice(1);
    // Début de la chaîne de sortie avec le nombre total d'étudiants
    let output = `Number of students: ${students.length}\n`;

    // Objet pour regrouper les étudiants par domaine d'étude
    const studentsByField = {};

    // Traitement de chaque ligne d'étudiant
    students.forEach(student => {
      // Destructuration du CSV : prénom, [nom ignoré], [age ignoré], domaine
      const [firstName, , , field] = student.split(',');
      // Création d'un tableau vide pour un nouveau domaine
      if (!studentsByField[field]) studentsByField[field] = [];
      // Ajout de l'étudiant dans son domaine
      studentsByField[field].push(firstName);
    });

    // Construction du rapport pour chaque domaine
    Object.keys(studentsByField).forEach(field => {
      output += `Number of students in ${field}: ${studentsByField[field].length}. ` +
                `List: ${studentsByField[field].join(', ')}\n`;
    });

    return output;
  } catch (error) {
    // En cas d'erreur (fichier non trouvé, problème de lecture, etc.)
    throw new Error('Cannot load the database');
  }
}

// Création de l'application Express
const app = express();

// Configuration de la route racine '/'
app.get('/', (req, res) => {
  // Envoi d'une réponse simple pour la page d'accueil
  res.send('Hello Holberton School!');
});

// Configuration de la route '/students'
app.get('/students', async (req, res) => {
  try {
    // Tentative de lecture et traitement du fichier CSV
    // process.argv[2] contient le chemin du fichier passé en argument
    const output = await countStudents(process.argv[2]);
    // Envoi de la réponse avec l'en-tête et les données
    res.send(`This is the list of our students\n${output}`);
  } catch (error) {
    // Gestion des erreurs : fichier non trouvé ou invalide
    res.send('This is the list of our students\nCannot load the database');
  }
});

// Démarrage du serveur sur le port 1245
app.listen(1245);

// Export de l'application pour les tests
module.exports = app;