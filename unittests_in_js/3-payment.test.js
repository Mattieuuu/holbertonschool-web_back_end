const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
  let spy;
  let consoleStub;

  beforeEach(function () {
    spy = sinon.spy(Utils, 'calculateNumber');
    consoleStub = sinon.stub(console, 'log');
  });

  afterEach(function () {
    spy.restore();
    consoleStub.restore();
  });

  it('should call Utils.calculateNumber with SUM, 100, 20 and log the result', function () {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledOnce(spy);
    sinon.assert.calledWithExactly(spy, 'SUM', 100, 20);
    sinon.assert.calledOnce(consoleStub);
    sinon.assert.calledWithExactly(consoleStub, 'The total is: 120');
  });
});
