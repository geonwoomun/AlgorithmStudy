

function solution(s) {
    const temp = s.slice(1, s.length-1).split('}');
    const tempList = [];
    const result = [];
    temp.forEach(value => {
        if (value.length === 0) return;
        let temp = '';
        let li = []
        for (let i=0; i < value.length; i++){
            if (isNumber(value[i])) {
                temp += value[i];
            }
            if ((value[i] === ',' || i === value.length -1) && temp !== '') {
                li.push(Number(temp));
                temp = '';
            }
        }
        tempList.push(li);
    });
    tempList.sort((a, b) => a.length - b.length );

    tempList.forEach(value => {
        value.forEach(value2 => {
            if (!result.includes(value2)){
                result.push(value2);
            }
        })
    })
    return result;
}

function isNumber(value){
    try{
        if(Number(value) >= 0) {
            return true;
        }
    }
    catch(e) {
        return false;
    }
}

const s = "{{20,111},{111}}"
console.log(solution(s));

console.log(Number('0'));