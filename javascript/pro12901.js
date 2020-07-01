function solution(a, b) {
  const days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  const day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'];

  let sum1 = 0;

  for (let i = 0; i < a - 1; i++) {
    sum1 += days[i];
  }

  const sum2 = (sum1 + b) % 7;
  const answer = day[sum2 > 0 ? sum2 - 1 : 6];
  return answer;
}

console.log(solution(5, 24));
