/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function (nums) {
  const numSet = new Set(nums);
  if (numSet.size < 3) return Math.max(...numSet);

  let i = 2;
  while (i--) {
    numSet.delete(Math.max(...numSet));
  }
  return Math.max(...numSet);
};
