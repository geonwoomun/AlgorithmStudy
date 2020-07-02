function solution(numbers, hand) {
  const direction = {
    left: [1, 4, 7],
    right: [3, 6, 9],
  };
  const numberPosition = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    '*': [3, 0],
    0: [3, 1],
    '#': [3, 2],
  };
  let left = numberPosition['*'];
  let right = numberPosition['#'];
  let answer = '';
  numbers.forEach((number) => {
    if (direction.left.includes(number)) {
      answer += 'L';
      left = numberPosition[number];
    } else if (direction.right.includes(number)) {
      answer += 'R';
      right = numberPosition[number];
    } else {
      let [x, y] = numberPosition[number];
      let [lx, ly] = left;
      let [rx, ry] = right;
      let leftDistance = Math.abs(x - lx) + Math.abs(y - ly);
      let rightDistance = Math.abs(x - rx) + Math.abs(y - ry);
      if (leftDistance > rightDistance) {
        right = [x, y];
        answer += 'R';
      } else if (rightDistance > leftDistance) {
        left = [x, y];
        answer += 'L';
      } else {
        if (hand === 'right') {
          right = [x, y];
          answer += 'R';
        } else {
          left = [x, y];
          answer += 'L';
        }
      }
    }
  });

  return answer;
}
