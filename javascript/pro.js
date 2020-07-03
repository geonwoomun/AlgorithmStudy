// 프로그래머스 level3 입국심사
function solution(n, times) {
  times.sort((a, b) => a - b);
  let left = 1;
  let right = n * times[times.length - 1];
  let answer = right;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    let count = 0;
    times.forEach((value) => {
      count += Math.floor(mid / value); // 한 사람당 몇명 할 수 있는지
      if (count >= n) {
        answer = Math.min(mid, answer);
        return;
      }
    });
    if (count >= n) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return answer;
}

console.log(solution(6, [7, 10]));

const arr = [1, 2, 3, 4, 5];
console.log(arr.slice(2, 4));
console.log(arr);
console.log(arr.splice(1, 3));
console.log(arr);
console.log(arr.concat([4, 5, 6]));
console.log(arr);
