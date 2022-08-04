const assert = require('assert');

const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  /* eslint-disable-next-line */
  it('should return the sum', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
