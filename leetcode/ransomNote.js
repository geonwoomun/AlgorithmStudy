// LeetCode ransomNote
var canConstruct = function(ransomNote, magazine) {
    let check = {};
    for(let i = 0; i < magazine.length; i++) {
        check[magazine[i]] = check[magazine[i]] ? check[magazine[i]] + 1 : 1;
    }
    for(let i = 0; i < ransomNote.length; i++) {
        if(check[ransomNote[i]]){
            check[ransomNote[i]] -= 1;
        }
        else {
            return false;
        }
    }
    return true;
};