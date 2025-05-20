const express = require('express');

// Création de l'application Express
const app = express();

// Route pour la page d'accueil
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Démarrage du serveur
app.listen(1245);

// Export de l'application pour les tests
module.exports = app;
