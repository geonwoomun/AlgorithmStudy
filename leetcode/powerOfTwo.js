const isPowerOfTwo = function (n) {
  if (n === 1) return true;
  let result = 1;
  while (true) {
    result *= 2;
    if (result === n) return true;
    else if (result > n) return false;
  }
};

const isPowerOfTwo1 = function (n) {
  if (n < 1) {
    return false;
  }
  return (n & (n - 1)) === 0;
};
