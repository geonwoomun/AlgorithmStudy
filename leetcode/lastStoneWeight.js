var lastStoneWeight = function(stones) {
  stones.sort((a,b) => a-b);
  while(stones.length > 1 ) {
    let x = stones.pop();
    let y = stones.pop();
    if(x !== y) {
        stones.push(x-y);
        stones.sort((a,b) => a-b);
    }
  }
  return stones.length ? stones[0] : 0;

};

console.log(lastStoneWeight([2,2]))