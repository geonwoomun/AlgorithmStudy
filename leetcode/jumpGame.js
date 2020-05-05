// LeetCode 점프게임

var canJump = function(nums) {
    let max = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (i > max) return false;
        
        if (i + nums[i] >= nums.length - 1) return true;
            
        max = Math.max(max, i + nums[i]);
    }
};
console.log(canJump([3,2,1,0,4]))