# Unit tests in JS

This project demonstrates basic unit testing in JavaScript using Mocha and Node's assert module.

## Setup

1. Install dependencies:
   ```sh
   npm install
   ```

2. Run tests:
   ```sh
   npm test ./0-calcul.test.js
   ```

## Files

- `0-calcul.js`: Implements `calculateNumber(a, b)` which rounds and sums two numbers.
- `0-calcul.test.js`: Mocha test suite for `calculateNumber`.
- `package.json`: Project configuration and test script.

## Example Usage

```js
const calculateNumber = require('./0-calcul');
console.log(calculateNumber(1, 3));     // 4
console.log(calculateNumber(1, 3.7));   // 5
console.log(calculateNumber(1.2, 3.7)); // 5
console.log(calculateNumber(1.5, 3.7)); // 6
```
