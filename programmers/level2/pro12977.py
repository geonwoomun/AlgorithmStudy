# 프로그래머스스 소수 만들기 
# 에라토스테네스의 체를 써서 제일 큰 3000 까지 소수인 애들은 1 아닌 애들은 0으로 두고
# 3개를 더했을 때의 dp[3개더한것] == 1인 애들은 소수이니깐 개수를 더 함.
import math
def solution(nums):
    answer = 0
    dp = [1 for i in range(3001)]
    dp[0] = 0
    dp[1] = 0
    for i in range(4,3001,2):
        dp[i] = 0
    for i in range(3, 3001, 2): # 소수가 아닌 애들은 0이 된다.
        if(dp[i] == 1) :
            for j in range(1,int(math.sqrt(i))+1,2):
                if(j == 1):
                    continue
                if(i != j and i % j == 0):
                    dp[i] = 0
                    break
      
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1) :
            for k in range(j+1, len(nums)):
                temp = nums[i] + nums[j] + nums[k]
                if(dp[temp] == 1):
                    answer +=1
    
    return answer