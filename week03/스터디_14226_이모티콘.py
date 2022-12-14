import sys
from collections import deque
input = sys.stdin.readline

S = int(input())    # 목표 이모티콘 갯수 받기 

# (화면에 현재 이모티콘, 클립보드 이모티콘) 형태로 입력받는다 
smileQueue = deque()
smileQueue.append((1,0))

# visited를 key:value로 짝지어 준다 
visited = dict()
visited[(1,0)] = 0


# BFS 
while smileQueue : 
    # 큐에서 꺼낸다
    screen, clip = smileQueue.popleft()
    
    # 화면에 이모티콘 개수가 S라면 
    if screen == S : 
        # 걸린 시간을 출력하고 루프 끝내기 
        print(visited[(screen, clip)])
        break
    
    # 동작별 분기점 나누기
    
    # 1. 화면에 있는 것 복사 
    if (screen, screen) not in visited.keys() : 
        visited[(screen, screen)] = visited[(screen, clip)] + 1
        smileQueue.append((screen, screen))
        
    # 2. 클립보드에 있는 것 모두 붙여넣기 
    if (screen + clip, clip) not in visited.keys() : 
        visited[(screen + clip, clip)] = visited[(screen, clip)] + 1
        smileQueue.append((screen + clip, clip))
        
    # 3. 화면에 있는 것 한개 삭제 
    if (screen - 1, clip) not in visited.keys() : 
        visited[(screen - 1, clip)] = visited[(screen, clip)] + 1
        smileQueue.append((screen - 1, clip))
        

# # =============visited list를 2-dimen-array로 저장하는 방법==================
# smileQueue = deque()
# smileQueue.append((1,0,0))

# visited = [[0]* 1001 for _ in range(1001)]
# visited[1][0] = 1

# while smileQueue : 
    
#     screen, clip, count = smileQueue.popleft()
    
#     if screen == S : 
#         print(count)
#         break
    
#     if visited[screen][screen] == 0 : # 복사하기 
#         visited[screen][screen] = visited[screen][clip] + 1
#         smileQueue.append((screen, screen, count + 1))
#     if visited[screen + clip][clip] == 0 and screen + clip <= S : #붙여넣기
#         visited[screen + clip][clip] = visited[screen][clip] + 1
#         smileQueue.append((screen + clip, clip, count + 1))
#     if visited[screen - 1][clip] == 0 and screen - 1 >= 0 : # 삭제하기 
#         visited[screen - 1][clip] = visited[screen][clip] + 1
#         smileQueue.append((screen - 1, clip, count + 1))
    