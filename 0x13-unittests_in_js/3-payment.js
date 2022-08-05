const { calculateNumber } = require('./utils');

module.exports = function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const totale = calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${totale}`);
};
