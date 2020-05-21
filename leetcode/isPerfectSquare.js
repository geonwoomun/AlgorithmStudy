var isPerfectSquare = function (num) {
  if (num < 2) return true;

  let left = 0;
  let right = num;
  let guess = 0;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    guess = mid * mid;

    if (guess === num) return true;

    if (guess > num) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return false;
};
