const { expect } = require('chai');
const request = require('request');
const app = require('./api');

describe('Index page', () => {
  let server;

  before((done) => {
    server = app.listen(7865, done);
  });

  after((done) => {
    server.close(done);
  });

  it('returns status code 200', (done) => {
    request('http://localhost:7865/', (err, res) => {
      expect(err).to.equal(null);
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('returns the correct message', (done) => {
    request('http://localhost:7865/', (err, res, body) => {
      expect(err).to.equal(null);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('returns 404 for unknown routes', (done) => {
    request('http://localhost:7865/unknown', (err, res) => {
      expect(err).to.equal(null);
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Cart page', () => {
  let server;

  before((done) => {
    server = app.listen(7865, done);
  });

  after((done) => {
    server.close(done);
  });

  it('returns status code 200 when :id is a number', (done) => {
    request('http://localhost:7865/cart/12', (err, res) => {
      expect(err).to.equal(null);
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('returns the correct message for a numeric cart id', (done) => {
    request('http://localhost:7865/cart/12', (err, res, body) => {
      expect(err).to.equal(null);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('returns status code 404 when :id is not a number', (done) => {
    request('http://localhost:7865/cart/hello', (err, res) => {
      expect(err).to.equal(null);
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
