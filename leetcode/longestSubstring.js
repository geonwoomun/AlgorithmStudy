// leetcode longeestSubstring

// 내 풀이... ㅠㅠ
var lengthOfLongestSubstring = function(s) {
    let temp = [];
    let maxLength = 0;

    for (let i = 0; i < s.length; i++) {
        if (temp.includes(s[i])){
            const index = temp.findIndex((value) => value === s[i]);
            temp = temp.slice(index+1);
            temp.push(s[i]);  
        }
        else {
            temp.push(s[i]);
        }
        maxLength = Math.max(maxLength, temp.length);
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