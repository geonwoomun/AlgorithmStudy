# 프로그래머스 폰켓몬
# 자바로 풀어봤엇는데 요즘엔 파이썬으로 공부중이니깐 파이썬으로 풀어본다.
# 정렬을 한다음에 마지막 숫자랑 다를 때만 숫자를 셌다.
# 그리고 nums의 길이 / 2 만큼만 고를 수 있으니 answer가 더 작을 때만.
# 같은 폰켓몬을 골랐을 때는 안 세도 되니깐 그냥 pass

def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums.sort()
    last = 0
    for value in nums :
        if(value != last and answer < length):
            answer +=1
            last = value
    return answer