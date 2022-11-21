# 동적 프로그래밍 
# 답 좀 봤다
import sys
input = sys.stdin.readline

T = int(input())    # test case 개수

def howMany(coins : list, M : int) : 
    numCoin = [0] * (M + 1) # 경우의 수 array
    numCoin[0] = 1
    for coin in coins : 
        for m in range(M + 1) : 
            # 아래단계 코인으로 M을 만드는 방법이 존재한다면 
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다,
            # 방법이 존재하지 않을 때에는 경우의 수는 그대로 
            if m >= coin : 
                numCoin[m] += numCoin[m - coin] 
    print(numCoin[M])                 
            


for testN in range(T) : 
    N = int(input())                        # 동전 종류 
    coins = map(int, input().split())       # 동전 목록
    M = int(input())                        # 만들어야 하는 금액
    howMany(coins, M)
    
