const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
  const url = 'http://localhost:7865/';

  it('should return status 200', function (done) {
    request.get(url, function (err, res, body) {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct message', function (done) {
    request.get(url, function (err, res, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', function () {
  const baseUrl = 'http://localhost:7865/cart/';

  it('should return status 200 and correct message for numeric id', function (done) {
    request.get(baseUrl + '12', function (err, res, body) {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 for non-numeric id', function (done) {
    request.get(baseUrl + 'hello', function (err, res, body) {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 for alphanumeric id', function (done) {
    request.get(baseUrl + '123abc', function (err, res, body) {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});

describe('/available_payments endpoint', function () {
  it('should return correct payment methods object', function (done) {
    request.get('http://localhost:7865/available_payments', { json: true }, function (err, res, body) {
      expect(res.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});

describe('/login endpoint', function () {
  it('should return correct welcome message', function (done) {
    request.post({
      url: 'http://localhost:7865/login',
      json: { userName: 'Betty' }
    }, function (err, res, body) {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});
