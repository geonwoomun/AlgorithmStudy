function solution(citations) {
  citations.sort((a, b) => a - b);

  let answer = 0;
  let length = citations.length;
  for (let i = 0; ; i++) {
    let index = citations.findIndex((s) => s >= i);
    if (length - index >= i && (index === 0 || citations[index - 1] <= i)) {
      answer = Math.max(answer, i);
    } else {
      break;
    }
  }

  return answer;
}
console.log(solution([3, 0, 6, 1, 5]));
