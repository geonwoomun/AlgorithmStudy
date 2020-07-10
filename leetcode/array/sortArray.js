/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function (A) {
  const evenArry = [];
  const oddArray = [];

  A.forEach((value) => {
    if (value % 2 === 0) {
      evenArry.push(value);
    } else {
      oddArray.push(value);
    }
  });
  return [...evenArry, ...oddArray];
};
