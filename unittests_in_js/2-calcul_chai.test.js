const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 for (1.4, 4.5)', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('should return 5 for (1.2, 3.7)', function () {
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    });
    it('should return 0 for (0, 0)', function () {
      expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    });
    it('should return -3 for (-1.2, -2.5)', function () {
      expect(calculateNumber('SUM', -1.2, -2.5)).to.equal(-3);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 for (1.4, 4.5)', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('should return -3 for (1.2, 3.7)', function () {
      expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
    });
    it('should return 0 for (0, 0)', function () {
      expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    });
    it('should return 1 for (1.4, 0.4)', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 0.4)).to.equal(1);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 for (1.4, 4.5)', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
    it('should return 0.25 for (1, 3.7)', function () {
      expect(calculateNumber('DIVIDE', 1, 3.7)).to.equal(0.25);
    });
    it('should return 0 for (0, 3.7)', function () {
      expect(calculateNumber('DIVIDE', 0, 3.7)).to.equal(0);
    });
    it('should return Error for (1.4, 0)', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
    it('should return Error for (1.4, 0.2)', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
    });
    it('should return -4 for (3.7, -1.2)', function () {
      expect(calculateNumber('DIVIDE', 3.7, -1.2)).to.equal(-4);
    });
  });
});
