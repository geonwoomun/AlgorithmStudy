function reduce(arr, func, start) {
  let i = start ? 0 : 1;
  let result = start || arr[0];

  for (; i < arr.length; i++) {
    result = func(result, arr[i], i, arr);
  }
  return result;
}
// const a = [1, 2, 3, 4, 5];

// console.log(reduce(a, (acc, cur) => acc + cur, 10));

// console.log(a.reduce((acc, cur) => acc + cur, 10));

const names = ['Alice', 'Bob', 'Tiff', 'Bruce', 'Alice'];
const func = (allNames, name) => {
  if (name in allNames) {
    allNames[name]++;
  } else {
    allNames[name] = 1;
  }
  return allNames;
};
console.log(reduce(names, func, {}));

console.log(names.reduce(func, {}));
