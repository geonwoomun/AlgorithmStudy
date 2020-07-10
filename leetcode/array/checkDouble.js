/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function (arr) {
  arr.sort((a, b) => {
    if (a > 0 || b > 0) return b - a;
    return a - b;
  });
  console.log(arr);
  const numsMap = new Map();
  let check = false;
  arr.forEach((value) => {
    if (numsMap.has(value * 2)) check = true;
    numsMap.set(value, 1);
  });
  return check;
};

console.log(checkIfExist([-3, -5, -7, 2, 6, 7]));
