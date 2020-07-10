/**
 * @param {number[]} A
 * @return {boolean}
 */
var validMountainArray = function (A) {
  let check = true;
  if (A.length < 3) return false;
  if (A[0] >= A[1]) return false;

  for (let index = 1; index < A.length - 1; index++) {
    if (check) {
      if (A[index] > A[index + 1]) check = false;
      if (A[index] === A[index + 1]) return false;
    } else {
      if (A[index] <= A[index + 1]) {
        return false;
      }
    }
  }
  if (check) return false;
  return true;
};

console.log(validMountainArray([0, 3, 2, 1]));
