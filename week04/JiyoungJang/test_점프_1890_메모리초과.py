# 게임판 길이 N
# =======================메모리 초과============================================
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input())

table = []
for n in range(N) : 
    table.append(list(map(int, input().split())))
    
# dp = [[0 for __ in range(N + 1)] for _ in range(N + 1)]    

# start = table[0][0]     # 시작점
def dynamic(y : int, x : int, table : list) : 
    if y > N - 1: 
        return 0
    elif x > N - 1: 
        return 0
    else : 
        value = table[y][x] 
        if value == 0 : 
            return 1    
        return dynamic(y, x + value, table) + dynamic(y + value, x, table)
    
    
    # # 가로로 이동
    # table[y][x + value]
    # dynamic(y, x + value, table)
    
    # # 세로로 이동 
    # table[y + value][x]
    # dynamic(y + value, x, table)
    
print(dynamic(0, 0, table))