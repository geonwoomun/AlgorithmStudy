// 카카오 무지의 먹방 라이브

function solution(food_times, k) {

    // 인덱스를 구해야 하기 때문에 value와 time으로 새로운 배열을 만들고 time 순으로 정렬을 해준다.
    let sortedArray = food_times.map((value, index) => ({time: value, index: index+1})).sort((a,b) => a.time - b.time);

    // 효율성을 통과하려면 k 값을 한번에 빼줘야함.
    for (let i = 0; i < food_times.length; i++) {
        let len = food_times.length - i;  // 현재 길이 - i    하면 앞에 다 먹은 부분은 제거하고 할 수 있음.
        let eatingTime = (sortedArray[i].time - (i === 0? 0: sortedArray[i-1].time)) * len; // 먹은 시간 * len을 하면 한번에 k 값을 계산해서 k를 뺄 수 있다. 
        // 처음의 경우에는 다 먹은 음식이 없기 때문에 0을 두고, 그 다음부터는 그 앞에 있던 시간을 빼줘야 제대로된 계산이 된다. 이미 앞에 시간만큼 지났다고 보기 때문에.
        // 그만큼의 시간 * len 만큼 지났다고 볼 수 있다.
        if ( k < eatingTime ) { // 만약 k 보다 크다면 i부터 자른 배열을 다시 index순으로 재정렬 하여 k % len을 나눈 것의 index를 출력하면된다.
            return sortedArray.slice(i).sort((a, b) => a.index - b.index)[k % len].index
        }
        // 아닐 경우 k를 eatingTime만큼 빼준다.
        k -= eatingTime;
    }
    return -1;
}

// 이분은 정말 똑똑하다.. 계속 보면서 다시 공부해야겠다.