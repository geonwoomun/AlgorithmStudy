function some(arr, func) {
  for (let i = 0; i < arr.length; i++) {
    if (func(arr[i], i, arr)) {
      return true;
    }
  }
  return false;
}
const arr = [1, 2, 3, 4, 5];
console.log(arr.some((value) => value > 2));
console.log(some(arr, (value) => value > 2));
console.log(arr.some((value) => value > 6));
console.log(some(arr, (value) => value > 6));

function every(arr, func) {
  for (let i = 0; i < arr.length; i++) {
    if (!func(arr[i], i, arr)) {
      return false;
    }
  }
  return true;
}
console.log(arr.every((value) => value > 3));
console.log(every(arr, (value) => value > 3));
console.log(arr.every((value) => value > 0));
console.log(every(arr, (value) => value > 0));
