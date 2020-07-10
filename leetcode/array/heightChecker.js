/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function (heights) {
  return [...heights]
    .sort((a, b) => a - b)
    .filter((value, index) => value !== heights[index]).length;
};
