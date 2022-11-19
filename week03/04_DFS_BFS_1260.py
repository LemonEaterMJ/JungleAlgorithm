# 그래프탐색기본 - DFS BFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

N, M, V = map(int, input().split())
# 정점 개수 N   /   간선 개수 M   /   탐색 시작 정점 번호 V


data = {}

# ****매우 중요*****
# 간선이 열결되지 않은 노드도 있을 수 있다! 
# 모든 노드를 시작할 때 dict에 입력해주자 
for i in range(1, N + 1) : 
    data[i] = []
        
for _ in range(M) : #간선 입력 
    start, end = map(int, input().split())
    
    data[start].append(end)
    
    data[end].append(start)
# Vortex : [연결된 vortex list]     dict key/value로 저장이 된다. 

for key in data.keys() : 
    data[key].sort()
    
# print(data)    

    

#==============DFS 실행하기=============
visited = []    # 방문한 노드 목록

def dfs(V : int, data : dict, visited : list) : # V : 탐색 시작 정점 
    print(V, end = ' ')
    visited.append(V)
    
    for i in data[V] : 
        if i not in visited : 
            dfs(i, data, visited)

dfs(V, data, visited)   
print()         
        

#============BFS 실행하기 ==============

visited = []


def bfs(V : int, data : dict, visited : list) : 
    needQ = deque()
    needQ.append(V) #탐색 시작 노드 입력 
    visited.append(V)
    
    # 앞으로 탐색해야 할 노드가 남아있다면,
    while needQ : 
        temp = needQ.popleft()  #목록 가장 앞을 꺼내고
        print(temp, end = ' ')
        visited.append(temp)    # 방문처리 
        
        # 그 노드의 인접노드들 중 방문하지 않은 곳들을 방문대기목록에 삽입
        for i in data[temp] : 
            if i not in visited : 
                needQ.append(i)
                visited.append(i)
    
bfs(V, data, visited)

