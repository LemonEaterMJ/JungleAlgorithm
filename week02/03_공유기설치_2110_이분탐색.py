import sys
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().split())
houseList = []

for i in range(0, N) : 
    houseList.append(int(input()))

houseList.sort()  
  

#시작값 설정 
start = 1
end = houseList[N - 1] - houseList[0]

# 체크 함수 
def check(diff : int) : 
    count = 1
    prev_house = houseList[0]
    for i in range(1, N) : 
        if houseList[i] - prev_house >= diff : 
            count += 1
            prev_house = houseList[i]
    if count >= C : 
        return True
    else : return False
        
    
    
    
while start <= end : 
    mid = (start + end) //2
    if check(mid) : # 이 거리로 공유기 C개 설치 가능합니다 
        start = mid + 1
    else : 
        end = mid - 1

print((start + end)//2)



# =================combination 풀이 : 메모리초과=================
# for house in range(0, N) : 
#     houseList.append(int(input()))
# houseList.sort()

# # 좌표들을 가지고 부분집합 뽑기
# # list 내의 각 원소들은 tuple    
# nCrHouse = list(combinations(houseList, C))


# minList = []
# #좌표 콤비 하나를 뽑습니다
# for combs in nCrHouse : 
#     minLength = combs[1] - combs[0]
#     for i in range(1, C) : 
#         if minLength > combs[i] - combs[i - 1] : 
#             minLength = combs[i] - combs[i - 1] 
#     # 각 콤비별 거리 최소값 
#     minList.append(minLength)

# print(max(minList))
            