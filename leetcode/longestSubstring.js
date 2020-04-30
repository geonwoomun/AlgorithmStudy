// leetcode longeestSubstring

// 내 풀이... ㅠㅠ
var lengthOfLongestSubstring = function(s) {
    let temp = [];
    let maxLength = 0;
    let lastElement = '';

    for (let i = 0; i < s.length; i++) {
        if (temp.includes(s[i])){
            if (lastElement === s[i]){
                temp = [s[i]];
            }
            else {
                const index = temp.findIndex((value) => value === s[i]);
                temp = temp.slice(index+1);
                temp.push(s[i]);
            }
            
        }
        else {
            temp.push(s[i]);
        }
        maxLength = Math.max(maxLength, temp.length);
        lastElement = s[i];
    }
    return maxLength;
};
// 코드 대박 !!!
var lengthOfLongestSubstring = function(s) {
    let longest = 0;
    let current = "";
    
    for (let i = 0; i < s.length; i++) {
        current = current.substring(current.indexOf(s[i]) + 1)        
        current += s[i];
        
        if (current.length > longest) {
            longest = current.length;
        }
    }
    
    return longest;
};

console.log(lengthOfLongestSubstring('dvdf'));