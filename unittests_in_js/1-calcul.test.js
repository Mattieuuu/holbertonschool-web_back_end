const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 for (1.4, 4.5)', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('should return 5 for (1.2, 3.7)', function () {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });
    it('should return 0 for (0, 0)', function () {
      assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    });
    it('should return -3 for (-1.2, -2.5)', function () {
      assert.strictEqual(calculateNumber('SUM', -1.2, -2.5), -3);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 for (1.4, 4.5)', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('should return -3 for (1.2, 3.7)', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
    });
    it('should return 0 for (0, 0)', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
    });
    it('should return 1 for (1.4, 0.4)', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 0.4), 1);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 for (1.4, 4.5)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('should return 0.25 for (1, 3.7)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1, 3.7), 0.25);
    });
    it('should return 0 for (0, 3.7)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 0, 3.7), 0);
    });
    it('should return Error for (1.4, 0)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
    it('should return Error for (1.4, 0.2)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error');
    });
    it('should return -4 for (3.7, -1.2)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 3.7, -1.2), -4);
    });
  });
});
