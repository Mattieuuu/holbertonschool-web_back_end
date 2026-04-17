const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('calls Utils.calculateNumber with the correct arguments', () => {
    const utilsSpy = sinon.spy(Utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    consoleSpy.restore();
    utilsSpy.restore();

    sinon.assert.calledOnceWithExactly(utilsSpy, 'SUM', 100, 20);
    sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 120');
  });
});