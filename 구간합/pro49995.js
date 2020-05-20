// 프로그래머스 Level4 쿠키 구입

function solution(cookie) {
  const temp = [0]; // 합들을 미리 계산해 놓음.
  let sum = 0;
  for (let i = 0; i < cookie.length; i++) {
    sum += cookie[i];
    temp.push(sum);
  }

  let max = 0;

  for (let m = 1; m < cookie.length; m++) {
    // temp의 길이는 쿠키보다 1크니 m 과 r의 범위를 이런식으로
    let left = temp[m];
    for (let r = m + 1; r <= cookie.length; r++) {
      let right = temp[r] - left;
      if (max >= right || left < right) continue; // max 가 더 크거나 right가 더크면 볼 필요 없음
      for (let l = 0; l < m; l++) {
        if (left - temp[l] < right) break; // 더 작으면 저 볼 필요 없음.
        if (left - temp[l] === right) {
          // 같으면 계산 후 그만.
          max = Math.max(max, right);
          break;
        }
      }
    }
  }

  return max;
}

const cookie = [1, 1, 2, 3];

console.log(solution(cookie));
