const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
  let stub;
  let consoleSpy;

  beforeEach(function () {
    stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(function () {
    stub.restore();
    consoleSpy.restore();
  });

  it('should stub Utils.calculateNumber to return 10 and log the correct message', function () {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledOnce(stub);
    sinon.assert.calledWithExactly(stub, 'SUM', 100, 20);
    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWithExactly(consoleSpy, 'The total is: 10');
  });
});
