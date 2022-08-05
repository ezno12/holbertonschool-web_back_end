/* eslint-disable jest/valid-expect */
const { expect } = require('chai');
const { spy } = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('utlis', () => {
  const CalSpy = spy(Utils, 'calculateNumber');
  /* eslint-disable-next-line */
  it('should call it', () => {
    sendPaymentRequestToApi(100, 20);
    /* eslint no-unused-expressions: ["error", { "allowTernary": true }] */
    expect(CalSpy.calledOnce).to.be.true;
    expect(CalSpy.calledWith('SUM', 100, 20)).to.be.true;
    CalSpy.restore();
  });
});
