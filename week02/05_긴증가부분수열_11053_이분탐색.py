import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
A.sort()
increasing = [A[0]]
count = 1
maxA = A[0]


for i in range(1, N) : 
    data = A[i]
    if maxA < data : 
        increasing.append(data)
        maxA = data
        count += 1

print(count)

# TODO : 오답임 왜 오답임????