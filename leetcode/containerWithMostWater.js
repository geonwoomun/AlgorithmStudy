// LeetCode Container with most water

var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let max = 0;
    
    while(left < right) {
        let h = Math.min(height[right], height[left]);
        max = Math.max(max, (right - left) * h);
        if(height[right] > height[left]) {
            left += 1;
        }
        else {
            right -=1;
        }
    }
    return max;
};