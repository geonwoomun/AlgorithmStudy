var findNumbers = function (nums) {
  return nums.reduce((acc, cur) => {
    if (String(cur).length % 2 === 0) {
      return acc + 1;
    }
    return acc;
  }, 0);
};
