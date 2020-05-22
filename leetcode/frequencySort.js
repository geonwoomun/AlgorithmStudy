var frequencySort = function (s) {
  const check = {};
  for (const str of s) {
    check[str] = check[str] ? check[str] + 1 : 1;
  }
  return Object.keys(check)
    .map((key) => [key, check[key]])
    .sort((a, b) => b[1] - a[1])
    .map((value) => {
      let str = '';
      for (let i = 0; i < value[1]; i++) {
        str += value[0];
      }
      return str;
    })
    .join('');
};
