import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())




# =================루트찾기 : 시간 초과 ===============================

nowA = A
nowB = B
moveL = 0
moveR = 0

while nowA != nowB : 
    if nowA > nowB : 
        moveL += 1
        nowA -= nowB
    elif nowA < nowB : 
        moveR += 1 
        nowB -= nowA 
    else : #nowA == nowB 즉 1,1
        break
print(moveL, moveR)


#================BFS : 메모리 초과남===========================

# q = deque()
# q.append((1,1))

# visited = dict()
# visited[(1,1)] = [0,0]


# while q : 
#     nowA, nowB = q.popleft()
    
#     if nowA == A and nowB == B : 
#         print(*visited[(nowA, nowB)])
#         break
    
#     moveL, moveR = visited[(nowA, nowB)]
#     if (nowA + nowB, nowB) not in visited.keys() and (nowA + nowB) <= A: 
#         visited[(nowA + nowB, nowB)] = [moveL + 1, moveR]
#         q.append((nowA + nowB, nowB))
        
#     if (nowA, nowA + nowB) not in visited.keys() and (nowA + nowB) <= B: 
#         visited[(nowA, nowA + nowB)] = [moveL, moveR + 1]
#         q.append((nowA, nowA + nowB))


