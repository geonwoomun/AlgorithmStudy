// LeetCode Jewels and Stones

var numJewelsInStones = function(J, S) {
  const check = {};
  for(let i = 0; i < S.length; i++) {
      check[S[i]] =  check[S[i]] ? check[S[i]] + 1 : 1; 
  }  
  let answer = 0;
  for(let j = 0; j < J.length; j++) {
      answer = check[J[j]] ? answer + check[J[j]] : answer;
  }
  return answer;
};