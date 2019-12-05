a = []

s = {}  # dictionary  key  value
# print(type("zzz"))
# print(type(123))

# a.append("zzz")
# a.append("sss")
# a.pop(0)
# 그냥 리스트만으로 스택과 큐를 구현 할수가 있따. 다만 조금 느리다.
# 스택은 뭐냐면 마지막에 쌓이고 빼낼때도 마지막것이 빠진다.  즉 append와 pop으로 구현가능
# 큐 는 마지막에 쌓이고 맨 앞에 것이 빠진다. 즉 append와 pop(0)으로 구현이 가능하다.

# dictionary 즉 사전 , 사전은 인덱스 , 즉 ㄱ ㄴ ㄷㄹ ㅁㅇㄹㄴㅁㅇㄹ key / value 

# s['zzz'] = 123
# s[123] = "zzz"
# print(s)

# print(s.items())

# for a, b in s.items():
#     print("key : " , a, "value : ", b)

# li = (1,2,3)

# a,b,c = li

# print(a,b,c)

# s = (1,2,3)

# print(s[0])

# 리스트 [ ] 연결리스트 , 배열과 비슷함.
# 튜플 () 리스트와 비슷한데 더하거나 빼기 불가능/ 대신에 빠름/
# 딕셔너리 {} key value 
# set {} 키값이 없다 value만 있다. 중복값을 알아서 제거해서 하나로 만들어요.

# visit = set()
# visit.add(1)
# visit.add(2)
# print(visit)

# for i in range(5,1, -1):  # 0~ 4까지
#     for j in range(4):
#         print(i*j)

# aaa = [1,2,3,4,5]

# for i in range(len(aaa)):
#     print(aaa[i])

# for v in aaa:
#     print(v)

# a = 4

# print(10 if a == 5 else 20)

# visit = set()

# visit.add(1)
# visit.add(2)
# visit.add(3)

# for i in range(10):
#     if(i not in visit):
#         print(i)

# a = 2
# xxxxxxxxxxx1
# 000000000001
# 000000000001   = 1 
# if a & 1 == 0 :
#     print("짝수입니다.")
# else :
#     print("홀수입니다.")

# if a % 2 == 0 :
#     print("짝수입니다.")
# else :
#     print("홀수입니다.")

from collections import deque, defaultdict # 덱 (큐와 스택을 합쳐놓은 애다.) defaultdict 얘는 딕셔너리를 만들 때 기본 값을 설정해주는 친구.

# q = deque()

# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# q.append(5)
# q.popleft() # 큐
# q.pop() # 스택
# print(q)

# dic = defaultdict(lambda:0) # 기본값

# dic[1] += 1
# print(dic)

# dic2 = {}
# # dic2[2] = []
# # dic2[2].append(2)
# # dic2[2].append(3)
# if(not dic2.get(2)):
#     dic2[2] = []
# else:
#     dic2[2].append(2)

# print(dic2)

# a = [1,5,4,3]

# a.sort(reverse=True)

# print(a)

# a = [[1,2],[4,2], [3,0],[0,1], [100,200]]

# a.sort(key=lambda x : (-x[1], x[0]), reverse = True)

# print(a)

# a = input() # input 느려 오소이 그래서 c++ cin  java scanner 이런 방법인거죠
import sys
input = sys.stdin.readline
# a = input()
# print(a)

# 길이는 k  am            5 7
# 5
# 7

# k = int(input()) # 스트링 받기 때문에
# m = int(input())
# k = list(map(int, input().split()))
# print(k)

n = 5
# 1
# 2
# 3
# 4
# 5
# l = []  l[1]

# for i in range(5):
#     l.append(int(input()))
# print(l)

# l = [_ for _ in range(n)] #[0,0,0,0,0] 

# for i in range(n):
#     l[i] = int(input())

# print(l)


# 이분 탐색 ?    
#   0  1  2  3  4  5  6  7  ~ 백개

#     5를 찾고 싶다.
#  보통 0 1 2 3 4 5 찾았다. 5번 찾아야한다.   80번
# 80
# 50     50 80    
# 51 100    75   80  
# 76  100   88      80
# 76   87   81    80 
# 76 80  78  
## 79 80  80  #




