# BOJ 2869 달팽이는 올라가고 싶다. 

from sys import stdin
input = stdin.readline

A,B,V = map(int, input().split())

print((V-B-1) // (A-B) + 1)

# 달팽이는 한밤에 A-B까지 올라갈 수 있다. 즉, (V-B-1) 까지를 A-B씩 가다가 A >= B+1 이기 때문에 +1 해주면 된다.