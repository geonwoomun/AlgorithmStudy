# 프로그래머스 42579 베스트앨범

from operator import itemgetter # dict의 item을 쉽게 가지고 올 수 있는 것인듯

def solution(genres, plays):
    album_dict = {} # 딕셔너리 안에 배열 또 그 안에 딕셔너리를 저장.
    genre_sum = {} # 딕셔너리 안에 장르별로 총합을 저장.
    for i in range(len(genres)): # 장르의 수 만큼.
        if genres[i] not in album_dict: # 장르가 앨범 딕셔너리에 없으면
            album_dict[genres[i]] = [{'play' : plays[i], 'i': i}] # 그장르를 만들고 처음 배열에 횟수랑 인덱스를 담은 딕셔너리를 넣음.
            genre_sum[genres[i]] = plays[i] # 그 플레이 수를 장르 sum에 넣음.
        else:
            album_dict[genres[i]].append({'play': plays[i], 'i': i}) # 원래 있으면 추가하고 플레이 횟수도 더함.
            genre_sum[genres[i]] += plays[i]

    genre_sum = sorted(genre_sum.items(), key=itemgetter(1), reverse = True)
    # genre_sum.items() 를 가지고 1번째 index를 가지고 내림차순으로 정렬.
    # genre_sum으로 dict로 바로 정렬하면 안 됨.

    result = []

    for i in genre_sum:  # genre_sum을 i 로 받아서서
        album_dict[i[0]] = sorted(album_dict[i[0]], key= lambda e: (-e['play'],e['i'])) # album 딕셔너리의 i[0]는 장르명, 즉 처음 장르를 play 큰거부터 i 작은거부터 정렬
        result.append(album_dict[i[0]][0]['i']) # 결과에다가 첫번째 녀석의 인덱스를 넣는다.
        if len(album_dict[i[0]]) >= 2: # 2개 이상이 있을경우엔 2번째 녀석도 넣는다. 2번째 까지만 있으니 0과 1의 인덱스로 가능.
            result.append(album_dict[i[0]][1]['i']) 
    # 반복하다 result 리턴.
    return result

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))