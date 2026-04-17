const Utils = {
  calculateNumber: function(type, a, b) {
    const aR = Math.round(a);
    const bR = Math.round(b);
    switch (type) {
      case 'SUM':
        return aR + bR;
      case 'SUBTRACT':
        return aR - bR;
      case 'DIVIDE':
        if (bR === 0) return 'Error';
        return aR / bR;
      default:
        throw new Error('Invalid operation type');
    }
  }
};

module.exports = Utils;
