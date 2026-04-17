const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  it('should return 4 for (1, 3)', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return 5 for (1, 3.7)', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return 5 for (1.2, 3.7)', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return 6 for (1.5, 3.7)', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should return 0 for (0, 0)', function () {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  it('should return -3 for (-1.2, -2.5)', function () {
    assert.strictEqual(calculateNumber(-1.2, -2.5), -3);
  });

  it('should return 2 for (1.4, 1.4)', function () {
    assert.strictEqual(calculateNumber(1.4, 1.4), 2);
  });

  it('should return 4 for (1.5, 1.5)', function () {
    assert.strictEqual(calculateNumber(1.5, 1.5), 4);
  });

  it('should return 2 for (1.49, 1.49)', function () {
    assert.strictEqual(calculateNumber(1.49, 1.49), 2);
  });

  it('should return 4 for (1.51, 1.51)', function () {
    assert.strictEqual(calculateNumber(1.51, 1.51), 4);
  });

  it('should return 1 for (0.4, 1.2)', function () {
    assert.strictEqual(calculateNumber(0.4, 1.2), 1);
  });

  it('should return 2 for (0.5, 1.2)', function () {
    assert.strictEqual(calculateNumber(0.5, 1.2), 2);
  });

  it('should return 2 for (0.4, 1.5)', function () {
    assert.strictEqual(calculateNumber(0.4, 1.5), 2);
  });

  it('should return 3 for (0.5, 1.5)', function () {
    assert.strictEqual(calculateNumber(0.5, 1.5), 3);
  });
});
