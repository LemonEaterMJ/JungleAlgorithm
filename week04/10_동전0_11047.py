# 그리디 알고리즘
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for _ in range(N) : 
    coins.append(int(input()))

# print(coins)

cnt = 0    
for nowCoin in reversed(coins) : 
    if nowCoin <= K : 
        moreC = K // nowCoin
        change = K % nowCoin
        K = change
        cnt += moreC
        if K == 0 : 
            break   
    
print(cnt)        
