/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function (n) {
  if (n === 0) return 0;
  let i = 0;
  while (n > 0) {
    i++;
    n -= i;
    if (n === 0) {
      return i;
    }
  }
  return i - 1;
};

console.log(arrangeCoins(5));
