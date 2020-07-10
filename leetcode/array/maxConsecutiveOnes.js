/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function (nums) {
  let cons = 0;
  let maxCons = 0;
  nums.forEach((value) => {
    if (value === 1) {
      cons++;
      maxCons = Math.max(cons, maxCons);
    } else {
      cons = 0;
    }
  });
  return maxCons;
};
