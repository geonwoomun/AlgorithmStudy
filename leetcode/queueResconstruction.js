// Input:
// [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

// Output:
// [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
var reconstructQueue = function (people) {
  let result = [];

  people
    .sort((a, b) => {
      if (a[0] === b[0]) {
        return a[1] - b[1];
      } else {
        return b[0] - a[0];
      }
    })
    .forEach((p) => {
      result.splice(p[1], 0, p);
    });

  return result;
};

console.log(
  reconstructQueue([
    [7, 0],
    [4, 4],
    [7, 1],
    [5, 0],
    [6, 1],
    [5, 2],
  ])
);
