# 위상정렬 
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# N명의 학생들   /   키를 비교한 횟수 M


graph = {}
# 연결선이 없는 경우를 포함하기 위해
# 모든 노드를 dict에 넣어준다 
for n in range(1, N + 1) : 
    graph[n] = []

# 연결선 입력

indegree = [0] * (N + 1)    #진입차수
for _ in range(M) : 
    big, small = map(int, input().split())
    
    # 방향성이 존재하기 때문에, 한쪽에만 입력
    graph[big].append(small)
    
    # 진입차수 카운트 
    indegree[small] += 1
    
# dict >> 학생번호 : [아래로 연결된 학생번호]   방향성 있는 graph 



def topology_sort(graph : dict, N : int) : 
    needQ = deque()
    visited = []
    
    # 1. 진입 차수가 0인 정점을 큐에 삽입한다
    for n in range(1, N + 1) : 
        if indegree[n] == 0 : 
            needQ.append(n)   # 대기큐에 삽입
    
    # 아직 방문대기가 남아있다면
    while needQ : 
        current = needQ.popleft()
        visited.append(current) # 방문판정
        
        # 2. 정점의 간선을 제거한다 
        for childN in graph[current] : 
            # 진입차수 제거 
            indegree[childN] -= 1
            
            # 진입차수 0이된 것들을 다시 방문대기에 집어넣는다
            if indegree[childN] == 0 : 
                needQ.append(childN)
    print(*visited)

topology_sort(graph, N)                

