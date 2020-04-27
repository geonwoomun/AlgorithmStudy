// 릿코드 twoSum

// 처음에 2중 포문으로 풀었다. 시간 복잡도가 O(n2)이었다.
// 솔루션을 보고 object를 이용해서 할 수 있을것 같아서 고쳐봤따.
// 시간초가 2배 이상 줄었다.
// 밑의 코드는 O(n)으로 돌아간다.

var twoSum = function(nums, target) {
    const obj = {};
    for (let i = 0; i < nums.length; i++) {
        obj[nums[i]] = i;
    }
    for (let j = 0; j < nums.length; j++){
        let complement = target - nums[j];
        if (obj[complement] && obj[complement] !== j){
            return [j, obj[complement]];
        }
    }
};