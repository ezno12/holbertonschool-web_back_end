const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculate numbers depend on operation type SUM', () => {
  /* eslint-disable-next-line */
  it('check out put of postive number', () => {
    assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    assert.strictEqual(calculateNumber('SUM', 1, 1), 2);
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  /* eslint-disable-next-line */
  it('check out put of negative numbers', () => {
    assert.strictEqual(calculateNumber('SUM', -1, 1), 0);
    assert.strictEqual(calculateNumber('SUM', -1.5, 0), -1);
  });
});
describe('check numbers depend on operation type SUBTRACT', () => {
  /* eslint-disable-next-line */
  it('check out put of postive number', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
    assert.strictEqual(calculateNumber('SUBTRACT', 4, 2), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
});
describe('check numbers depend on operation type DIVIDE', () => {
  /* eslint-disable-next-line */
  it('check out put of postive number', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 0, 2), 0);
    assert.strictEqual(calculateNumber('DIVIDE', 2, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 4, 2), 2);
  });
  /* eslint-disable-next-line */
  it('check out put of postive number', () => {
    assert.strictEqual(calculateNumber('DIVIDE', -1, 1), -1);
  });
});
