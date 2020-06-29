/**
 * @param {number[]} nums
 * @return {number}
 */
const findDuplicate = function (nums) {
  const numsMap = new Map();

  nums.forEach((num) => {
    numsMap.set(num, 1 + (numsMap.get(num) || 0));
  });

  return [...numsMap.entries()].filter((entry) => entry[1] > 1)[0][0];
};

console.log(findDuplicate([1, 3, 4, 2, 2]));
