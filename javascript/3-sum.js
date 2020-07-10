/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  const result = new Map();
  for (let std = 0; std < nums.length; std++) {
    let start = std + 1;
    let end = nums.length - 1;
    while (start < end) {
      const sum = nums[std] + nums[start] + nums[end];
      if (sum > 0) {
        end -= 1;
      } else if (sum < 0) {
        start += 1;
      } else {
        if (!result.has(`${nums[std]}${nums[start]}${nums[end]}`))
          result.set(`${nums[std]}${nums[start]}${nums[end]}`, [
            nums[std],
            nums[start],
            nums[end],
          ]);
        start += 1;
      }
    }
  }
  return [...result.values()];
};
