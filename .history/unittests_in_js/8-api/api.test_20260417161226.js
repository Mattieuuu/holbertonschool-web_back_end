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
