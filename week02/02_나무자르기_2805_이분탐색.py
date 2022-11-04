import sys
input = sys.stdin.readline

#나무수 N, 필요한나무길이 M
N, M = map(int, input().split())
treeList = list(map(int, input().split()))

# 시작값 설정 
start = 0
end = max(treeList)

# 가능 여부 체크
def check(chopHeight : int) : 
    sumTree = 0
    for tree in treeList : 
        x = tree - chopHeight
        if x >= 0 : 
            sumTree += x
    if sumTree >= M : 
        return True
    else : return False 
    
while start <= end : 
    mid = (start + end) // 2
    if check(mid) : # 이 높이에서 자르면 가능합니다
        start = mid + 1
    else : #불가능합니다 
        end = mid - 1 #그럼 높이를 좀 내려보죠
mid = (start + end) // 2
    
print(mid)