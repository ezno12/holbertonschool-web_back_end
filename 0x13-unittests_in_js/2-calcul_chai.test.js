/* eslint-disable jest/valid-expect */
const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculate numbers depend on operation type SUM', () => {
  /* eslint-disable-next-line */
  it('check out put of postive number', () => {
    expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    expect(calculateNumber('SUM', 1, 1)).to.equal(2);
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  /* eslint-disable-next-line */
  it('check out put of negative numbers', () => {
    expect(calculateNumber('SUM', -1, 1)).to.equal(0);
    expect(calculateNumber('SUM', -1.5, 0)).to.equal(-1);
  });
});
describe('check numbers depend on operation type SUBTRACT', () => {
  /* eslint-disable-next-line */
  it('check out put of postive number', () => {
    expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    expect(calculateNumber('SUBTRACT', 4, 2)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
});
describe('check numbers depend on operation type DIVIDE', () => {
  /* eslint-disable-next-line */
  it('check out put of postive number', () => {
    expect(calculateNumber('DIVIDE', 0, 2)).to.equal(0);
    expect(calculateNumber('DIVIDE', 2, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 4, 2)).to.equal(2);
  });
  /* eslint-disable-next-line */
  it('check out put of postive number', () => {
    expect(calculateNumber('DIVIDE', -1, 1)).to.equal(-1);
  });
});
