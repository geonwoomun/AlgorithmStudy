var findJudge = function (N, trust) {
  const check = {};
  for (let i = 1; i <= N; i++) {
    check[i] = [];
  }

  trust.forEach((people) => {
    check[people[0]].push(people[1]);
  });

  const checkArray = Object.keys(check);
  let judge = checkArray.find((key) => check[key].length === 0);

  if (!judge) {
    return -1;
  }
  let checkInclude = true;
  checkArray.forEach((key) => {
    if (key !== judge) {
      if (!check[key].includes(Number(judge))) {
        checkInclude = false;
      }
    }
  });

  return checkInclude ? judge : -1;
};

console.log(findJudge(2, [[1, 2]]));
