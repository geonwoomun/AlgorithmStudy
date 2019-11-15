# 프로그래머스 기능개발

def solution(progresses, speeds):
    answer = []
    temp = [0 for i in range(len(progresses))] # 0이면 배포 안 된것. 1이면 배포한것.
    check = False # 다 했는지 체크하는 것.
    while(1):
        num = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i] # 스피드만큼을 계속 더해준다.
            if(progresses[i] >=100 and temp[i] == 0): # 100 이상 이고 자신의 temp[i] 가 0 즉 배포 안 됐을 때
                if(i == 0): # 첫번째 녀석이면 그냥 배포 해도 됨.
                    temp[i] = 1
                    num +=1
                elif(temp[i-1] == 1): # 첫번째가 아니면 자기 앞이 배포가 된 상태여야함.
                    if(i == len(progresses)-1): # 마지막이면 check 를 트루로
                        check = True
                    temp[i] = 1 # 자기껄 배포하고 숫자 늘림.
                    num +=1
        if(num !=0):
            answer.append(num)
        if(check == True):
            break
            
    return answer
