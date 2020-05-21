var singleNonDuplicate = function (nums) {
  let check = {};
  nums.forEach((value) => {
    check[value] = check[value] ? check[value] + 1 : 1;
  });
  return Object.keys(check).find((key) => check[key] === 1);
};
