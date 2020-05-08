// LeetCode Group Anagrams

var groupAnagrams = function(strs) {
    let check = {};
    for(let str of strs) {
        let key = [...str].sort().join('');
        if (!check[key]) {
            check[key] = []
        }
        check[key].push(str);
    }
    return Object.values(check);
};

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))