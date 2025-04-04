# JavaScript ES6 Data Manipulation

## 1. Map() en JavaScript
Quand et comment l'utiliser ? La méthode map() est utilisée pour créer un nouveau tableau à partir d'un tableau existant, en transformant chaque élément. C'est comme si tu avais un tableau de nombres et que tu voulais les multiplier par 2. Par exemple :

```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map(num => num * 2);
console.log(doubled);  // [2, 4, 6]
```

## 2. Filter() en JavaScript
Quand et comment l'utiliser ? La méthode filter() permet de créer un nouveau tableau contenant seulement les éléments qui satisfont une certaine condition. Par exemple, si tu veux garder que les nombres pairs dans un tableau :

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers);  // [2, 4, 6]
```

## 3. Reduce() en JavaScript
Quand et comment l'utiliser ? La méthode reduce() permet de réduire un tableau en un seul élément, en appliquant une fonction à chaque élément. Par exemple, pour additionner tous les nombres d'un tableau :

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum);  // 10
```

## 4. Typed Arrays en JavaScript
Qu'est-ce que c'est ? Un typed array est un tableau spécial qui peut stocker des types de données spécifiques comme des entiers ou des flottants. Cela permet de travailler plus efficacement avec de grandes quantités de données binaires, comme les images ou les vidéos.

Quand les utiliser ? Tu les utilises quand tu travailles avec des données binaires ou quand tu veux que ton tableau stocke un type de donnée particulier comme des entiers.

Caractéristiques :
- Taille fixe
- Chaque élément a un type spécifique (comme Int8Array, Float32Array, etc.)
- Les éléments sont stockés de manière compacte pour plus d'efficacité.

## 5. Set en JavaScript
Qu'est-ce qu'un Set ? Un Set est une collection de valeurs uniques. Par exemple, un Set ne peut pas avoir de doublons, même si tu essaies d'ajouter plusieurs fois le même élément.

Caractéristiques principales :
- Chaque élément est unique.
- L'ordre des éléments est conservé, mais il ne peut pas y avoir de répétition.

Exemple d'utilisation :
```javascript
const mySet = new Set();
mySet.add(1);
mySet.add(2);
mySet.add(2);  // Ce 2 ne sera pas ajouté car il est déjà dans le set
console.log(mySet);  // Set { 1, 2 }
```

## 6. Map en JavaScript
Qu'est-ce qu'un Map ? Un Map est une collection de paires clé-valeur. Tu peux utiliser n'importe quel type de donnée pour les clés (pas juste des chaînes de caractères comme avec les objets classiques).

Exemples d'utilisation :
```javascript
const grades = new Map();
grades.set('Alice', 90);
grades.set('Bob', 85);
console.log(grades.get('Alice'));  // 90
```

## ES6 Promises

### 7. Asynchrone / Synchrone
Qu'est-ce que c'est ?
- Synchrone : Les actions se passent une par une. Si quelque chose prend du temps, cela bloque le reste.
- Asynchrone : Les actions se passent en parallèle. Si quelque chose prend du temps, cela ne bloque pas le reste.

### 8. Qu'est-ce qu'une Promise ?
Une Promise est une promesse de faire quelque chose à l'avenir. Elle commence dans un état "en attente" et peut finir par réussir ou échouer.

### 9. Les états d'une Promise
- Pending (en attente) : La promesse est en cours.
- Fulfilled (réussie) : La promesse a réussi.
- Rejected (échouée) : La promesse a échoué.

### 10. Chainer des Promises
Oui, on peut chainer des promises. C'est utile quand on veut enchaîner plusieurs actions asynchrones, comme une tâche après l'autre.

Exemple de chaine de promises :
```javascript
fetch('data.json')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erreur:', error));
```

### 11. Quand utiliser try / catch ?
try et catch sont utilisés pour gérer les erreurs. Tu mets ton code dans un try, et s'il y a une erreur, elle est attrapée dans le catch.

Exemple :
```javascript
try {
  let result = riskyFunction();
} catch (error) {
  console.log('Erreur attrapée:', error);
}
```

### 12. Quand utiliser async / await ?
Tu utilises async et await pour rendre ton code asynchrone plus lisible. Par exemple, pour attendre la réponse d'une requête HTTP avant de continuer à exécuter le reste du code.

Exemple :
```javascript
async function fetchData() {
  let response = await fetch('data.json');
  let data = await response.json();
  console.log(data);
}
```

## JavaScript DOM Manipulation

### 13. Est-ce que JavaScript est interprété ou compilé ?
JavaScript est interprété. Cela signifie que le navigateur lit et exécute le code ligne par ligne.

### 14. Quand JavaScript est-il apparu et pourquoi ?
JavaScript est apparu en 1995. Il a été créé pour rendre les pages web interactives et dynamiques.

### 15. Qu'est-ce que le DOM ?
DOM signifie "Document Object Model". C'est une représentation de la structure HTML d'une page web sous forme d'objets.

### 16. Comment cibler des éléments avec JavaScript ?
- getElementById : Pour cibler un élément par son id.
- getElementsByClassName : Pour cibler tous les éléments avec une classe donnée.
- querySelector : Pour cibler un élément avec un sélecteur CSS.

### 17. Qu'est-ce qu'un pseudo-classe CSS ?
Une pseudo-classe CSS permet de cibler un élément selon son état. Par exemple, :hover pour cibler un élément lorsqu'on passe la souris dessus.

Exemple :
```css
button:hover {
  color: red;
}
```

### 18. Le fetch API
Le fetch API est utilisé pour récupérer des données depuis un serveur, par exemple, pour charger un fichier JSON.

Synchronous ou asynchronous ? fetch est asynchrone, ce qui veut dire qu'il n'arrête pas le reste du code pendant qu'il attend la réponse du serveur.