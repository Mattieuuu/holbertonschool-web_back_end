const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.status(200).send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
  res.status(200).send(`Payment methods for cart ${req.params.id}`);
});

if (require.main === module) {
  app.listen(7865, () => {
    console.log('API available on localhost port 7865');
  });
}

module.exports = app;
