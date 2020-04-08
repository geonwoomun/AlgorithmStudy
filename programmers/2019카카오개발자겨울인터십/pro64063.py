import sys
sys.setrecursionlimit(10000000)

def findEmptyRoom(number, rooms):
    if number not in rooms:
        rooms[number] = number + 1
        return number
    
    empty = findEmptyRoom(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty


def solution(k, room_number):
    answer = []
    rooms = dict()

    for number in room_number:
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)
    
    return answer

k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))