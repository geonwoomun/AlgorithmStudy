# 프로그래머스 입국심사
# 어려워서 다른 사람 코드를 참고 했습니다.
# 이분탐색 문제라고 적혀있었지만 다르게 풀어볼까 해서 다르게 풀어보다 실패.
# 잘 모르겠어서 블로그 참고. 참고한거를 더 리팩토링해서 짧게 만들었다.

def solution(n, times):
    count = 0
    times.sort() # 오름차순 정렬.
    low = 1
    high = times[-1] * n
    md_list = [] # 충분히 할 수 있을 때 값을 넣음.
    while(low <= high): # 이분 검색 하듯이.
        mid = (low + high) // 2 # 가운데 값으로.
        for time in times:
            count += mid // time # 가운데 값일 때 심사관이 처리 할 수 있는 양. 크거나 같으면 추가한다.
            if count >= n: # count 커지거나 같으면 추가하고 for 문 끝낸다.
                md_list.append(mid)
                break
        if(count >= n): # count 가 크거나 같으면 이제 더 작은 애를 찾아야 하기 때문에 high를 mid-1로 해서 찾아본다.
            high = mid -1 # n이 더 클 경우 high가 크다는 뜻이므로 mid-1로 만들어줌. 같아졌을 때도 더 작은애가 있을수 있기때문에 -1해서 찾아보자.
            count = 0 
        elif count < n : # 아직 n 이 클 경우 low가 너무 작다는 뜻이므로 mid+1로 만들어줌.
            low = mid + 1
            count = 0
    return min(md_list) # 제일 작은 값을 출력.

print(solution(6, [7,10]))