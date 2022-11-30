import sys
input = sys.stdin.readline

N, M = map(int, input().split())

horCnt = 0


for _ in range(N) : 
    floorLine = input().rstrip('\n').split('|')
    
    
