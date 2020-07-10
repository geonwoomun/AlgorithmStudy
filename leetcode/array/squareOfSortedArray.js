/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortedSquares = function (A) {
  return A.map((v) => v ** 2).sort((a, b) => a - b);
};

console.log(sortedSquares([-4, -1, 0, 3, 10]));
