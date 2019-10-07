# i         1      2     3

#  vi       60    100    120         가치
#  wi       10    20      30         무게
#  vi/wi    6     5        4         무게 대비 가치

#  js 코드

#     var test = [[1,60,10], [2,100,20], [3,120,30]];
#     function fractionalKnapsack(item, w) {   // 아이템들과 최대 무게를 받아서
#       var sorted = item.sort(function(prev, cur) {
#         return cur[1] / cur[2] - prev[1] / prev[2]; // 무게 대비 가치 순으로 정렬
#       });
#       var limit = w;      // 무게를 뺄거임.
#       var result = 0;    // 가치를 더할거임
#       for (var i = 0; i < sorted.length; i++) {
#         var cur = sorted[i];
#         if (limit > 0) {
#           if (limit >= cur[2]) { // 물건 무게가 제한 이하일 경우
#             limit -= cur[2];
#             result += cur[1]; 
#           } else { // 물건 무게가 제한 초과일 경우
#             result += cur[1] / cur[2] * limit; // 잘라서 넣음   무게 대비 가치는 1개의 무개일 때 가치니깐 limit 만큼 넣을 수 있다.
#             limit = 0;  // limit는 이제 0이 되고 끝.
#           }
#         } else {
#           break;
#         }
#       }
#       return result;
#     }
#     fractionalKnapsack(test, 50); // 240

test = [[1,60,10], [2,100,20], [3,120,30]]

def fractionalKnapsack(item, w):
    item = sorted(item, key=lambda x:x[1]/x[2], reverse=True) # item을 받은거를 x[1]/x[2]의 역순으로 정렬
    limit = w # 최대 담을 수 있는 무게
    result = 0 # 결과 얼마나 담았는지
    for value in item:  #item list에서 하나씩 받아와서
        if(limit > 0):  # limit 가 0보다 크면 즉 아직 더 담을 수 있을 때
            if(limit >= value[2]): # 총 무게가 limit 보다 작으면 즉 한번에 다 담을 수 잇으면
                limit -= value[2] # 한번에 다담고 limit에서 무게를 빼고
                result += value[1] # 결과에 값을 담고
            else:
                result += value[1] / value[2] * limit # 만약에 한번에 다 담을 수 없으면 limit 양만큼 잘라서 넣는다. 무게당 가치 x limit 남은 양
                limit = 0
        else: ## limit 가 0보다 작으면 끝
            break
    
    return result

print(fractionalKnapsack(test, 50))
