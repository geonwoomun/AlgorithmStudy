var isPowerOfTwo = function (n) {
  if (n === 1) return true;
  let result = 1;
  while (true) {
    if (result === n) return true;
    else if (result > n) return false;
    result *= 2;
  }
};

var isPowerOfTwo1 = function (n) {
  if (n < 1) {
    return false;
  }
  return (n & (n - 1)) == 0;
};
