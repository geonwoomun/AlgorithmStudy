/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] >= target) {
      return i;
    }
  }
  return nums.length;
};

var searchInsert = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;
  let middle = Math.floor((left + right) / 2);
  while (nums[middle] !== target && left <= right) {
    if (target < nums[middle]) {
      right = middle - 1;
    } else {
      left = middle + 1;
    }
    middle = Math.floor((left + right) / 2);
  }
  return nums[middle] === target ? middle : left;
};
