// var wordBreak = function(s, wordDict) {
//     for(const v of wordDict) {

//     }
// };

var wordBreak = function(s, wordDict) {
	for (let i = 0; i < wordDict.length; i++) {
        let v = s.split(wordDict[i]);
        console.log(v);
        s= v.join('.');
        // s = s.split(wordDict[i]).join('.');
    }
    console.log(s);
    return s.split('.').join('').length === 0;
};
const a = 'leetcode';
console.log(a.substring(0,2));
console.log(a);
const b = ['leet','code'];

console.log(wordBreak(a,b))