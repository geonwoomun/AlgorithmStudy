// var checkValidString = function(s) {
//     let countRisk = 0;
//     const stack = [];
//     for(const str of s) {
//         if(stack.length === 0) {
//             stack.push(str);
//             continue;
//         }
//         if(str === '(') {
//             stack.push(str);
//         }
//         else if(str === ')') {
//             if(stack[stack.length-1] === '(') {
//                 stack.pop();
//             }
//             else if(stack[stack.length-1] === '*') {
//                 stack.pop();
//             }
//         }
//        else {
//         if(stack[stack.length-1] === '('){
//             stack.pop();
//         }
//         else{
//             stack.push(str);
//             countRisk +=1;
//         }
//        }
//     }
//     while(countRisk > 0) {
//         if(stack[stack.length-1] === "*") {
//             stack.pop();
//         }
//         else {
//             stack.pop();
//             countRisk -= 1;
//         }
//     }
//     return !stack.length
// };

console.log([].findIndex(e => e ==1));