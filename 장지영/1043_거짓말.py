import sys
input = sys.stdin.readline

N, M = map(int, input().split())

truList = list(map(int, input().split()))   
# [0] 사람 수 , [1~] 사람 번호

# index : party number / [0] ppl number / [1~] ppl name
parties = [[0, 0]]


truParties = []

for _ in range(1, M + 1) : 
    parties.append(list(map(int, input().split())))
    for i in range(1, truList[0]) : 
        if truList[i] in parties[_][1:] : 
            print(parties[_])


