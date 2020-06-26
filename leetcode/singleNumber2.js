/**
 * @param {number[]} nums
 * @return {number}
 */
const singleNumber = function (nums) {
  let result = 0;
  const numMap = new Map();
  nums.forEach((num) => {
    if (numMap.has(num)) {
      numMap.set(num, numMap.get(num) + 1);
    } else {
      numMap.set(num, 1);
    }
  });
  let entries = numMap.entries();
  return [...entries].filter((entry) => entry[1] === 1)[0][0];
  //   for (let i = 0; i < numMap.size; i++) {
  //     const [key, value] = entries.next().value;
  //     if (value === 1) return key;
  //   }
};

console.log(singleNumber([0, 1, 0, 1, 0, 1, 99]));
