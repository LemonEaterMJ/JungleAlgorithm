import sys
# from itertools import combinations
input = sys.stdin.readline

N = int(input())

liqList = list(map(int, input().split()))
liqList.sort()

# 초기 포인터
start = 0
end = N - 1

minNum = 2000000000
minLiqs = [0, 0]

while start < end : 
    A = liqList[start]
    B = liqList[end]
    mixChar = abs(A + B)
    if mixChar <= minNum : 
        minNum = mixChar
        minLiqs[0] = A
        minLiqs[1] = B
    if abs(A) > abs(B) : 
        start += 1
    elif abs(A) < abs(B) : 
        end -= 1
    else : # 두 숫자의 절대값이 같을 때 = 특성 0
        break

        
print(*minLiqs)    





# # 둘씩 짝지은 콤비네이션을 list로 받는다 
# mixLiqs = list(combinations(list(map(int, input().split())), 2))
# L = int(N*(N-1)/2)   #length of mixLiqs


# start = 0
# end = 2000000000

# # +-liqChar 특성을 가진 혼합용액을 만들 수 있습니까?
# def check(liqChar : int) : 
#     for i in range(0, L) : 
#         if abs(sum(mixLiqs[i])) <= liqChar :
#             return i # combination index 
#     return -1 
        

# while (start <= end) : 
#     mid = (start + end) // 2
#     index = check(mid)
#     if index < 0 : # 없습니다 > mid 를 0에서 떨어뜨려야겠군요
#         start = mid + 1
#     else : 
#         # 만들수 있습니다 > mid를 0에 더 가까이 붙여보죠
#         end = mid - 1 
        
# print(*mixLiqs[index])
    