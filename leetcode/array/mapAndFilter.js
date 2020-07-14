function map(arr, func) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(func(arr[i], i));
  }
  return result;
}

function filter(arr, func) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    func(arr[i], i) && result.push(arr[i]);
  }
  return result;
}
const arr = [1, 2, 3, 4, 5];
console.log(map(arr, (value) => value + 2));
console.log(filter(arr, (value) => value > 2));
