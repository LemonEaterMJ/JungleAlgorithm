import sys
input = sys.stdin.readline
import heapq

# Char number N, risable lv sum K
N, K = map(int, input().split())

charList = []
for _ in range(N) : 
    heapq.heappush(charList, int(input()))

nowMin = []    
while K : 
    nowMin.append(heapq.heappop(charList))
    if charList[0] == nowMin[0] : 
        nowMin.append(heapq.heappop(charList))
    
    howMany = len(nowMin)    
    diff = charList[0] - nowMin[0]
    
    if diff > K : 
        for m in range(howMany - 1) : 
            heapq.heappush(charList, nowMin[m] + (K // howMany))
        heapq.heappush(charList, nowMin[howMany - 1] + K // howMany + K % howMany)
    else : # 0 < diff < K
        
print()