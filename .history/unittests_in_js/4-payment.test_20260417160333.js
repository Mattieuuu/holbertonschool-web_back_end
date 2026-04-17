const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  it('stubs Utils.calculateNumber and logs the stubbed result', () => {
    const utilsStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnceWithExactly(utilsStub, 'SUM', 100, 20);
    sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 10');

    consoleSpy.restore();
    utilsStub.restore();
  });
});