# 그래프탐색기본 - 최소신장트리 - 크루스칼 알고리즘
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
# 정점 개수 V   /   간선 개수 E

edgeList = []
vertexList = [0] * (V + 1)

for j in range(1, V + 1) : 
    # V개의 정점에 대해 부모 확인용 리스트 만들기 
    # index j : 정점 번호(이름)    /   값 : 부모 정점
    vertexList[j] = j

for i in range(E) : # E개의 간선 정보 
    # 시작 정점 [0]   /   끝 정점 [1]   /   간선 가중치 [2]
    edgeList.append(list(map(int, input().split())))
    

# 간선 가중치 순서로 정렬    
edgeList.sort(key = lambda x:x[2])

# ===========부모 찾기 함수 ================
def findParent(vertexList : list, index : int) : 
    if vertexList[index] != index : 
        vertexList[index] = findParent(vertexList, vertexList[index])
    return vertexList[index]

def unionParent(vertexList : list, indexA : int, indexB : int) : 
    aParent = findParent(vertexList, indexA)
    bParent = findParent(vertexList, indexB)
    if aParent < bParent :  
        vertexList[bParent] = aParent
    else : 
        vertexList[aParent] = bParent


countValue = 0  #간선 총합 가중치 
# 간선 연결 
for x in range(E) : 
    # A, B들의 index 
    indexA = edgeList[x][0]
    indexB = edgeList[x][1]
    
    #find 연산 후 cycle이 아니라면 union 연산
    if findParent(vertexList, indexA) != findParent(vertexList, indexB) : 
        unionParent(vertexList, indexA, indexB)
        # 간선 연결됨, 간선 가중치 총 합에 더해주기 
        countValue += edgeList[x][2]
    else : 
        continue
    

print(countValue)
        
        

