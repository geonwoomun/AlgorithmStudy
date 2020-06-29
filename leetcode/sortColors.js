var sortColors = function (nums) {
  const numsMap = new Map();
  nums.forEach((num) => {
    numsMap.set(num, 1 + (numsMap.get(num) || 0));
  });
  let i = 0;
  [0, 1, 2].forEach((value) => {
    console.log(numsMap.get(value));
    console.log(value);
    let count = numsMap.get(value);
    while (count--) {
      nums[i++] = value;
    }
  });
};

console.log(sortColors([2, 0, 2, 1, 1, 0]));
