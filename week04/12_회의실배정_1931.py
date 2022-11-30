# 그리디 알고리즘
import sys
input = sys.stdin.readline

N = int(input())    # 회의의 갯수 

# 빨리 끝나는 순서대로 회의를 정렬해야한다 
# 끝나는 시간이 같다면 시작시간이 빠른순으로 정렬 

meetings = []

for i in range(N) : 
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key=lambda x : (x[1], x[0]))

count = 1
endTime = meetings[0][1]
for j in range(1, N) : 
    if meetings[j][0] >= endTime : 
        count += 1
        endTime = meetings[j][1]

print(count)






# 알고리즘 자체는 위에 정답이랑 비슷한데, 필요없는걸 안빼고 돌려서 무거워짐 
# 매 순간의 최적해가 정답으로 이어지기 때문에, 최적해가 아닌걸 고려할 필요는 없는듯
# ========맞은지는 모르겠고 시간초과 나옴=================
# 가능 경우의수를 전부 세서 max 돌리는 방법 

# meetings = []
# plans = []
# count = 0
# for i in range(1, N + 1) : 
#     start, end = map(int, input().split())
#     meetings.append([start, end])
    
#     flag = 0
#     if i == 0 : 
#         plans.append([start, end])
#         flag = 1
#         count = 1
#     else : 
#         for plan in plans : 
#             if start >= plan[-1] : # 바로 앞 회의끝 이후 시작한다면 
#                 plan.extend([start, end])
#                 flag = 1
#         if flag == 0 : # 어떤 회의 뒤에도 추가될 수 없다면 
#             # 새로운 plan의 시작점이 된다 
#             plans.append([start, end])
            
# # print(plans)
# result = []
# for p in plans : 
#     result.append(len(p) // 2)
    
# print(max(result))

            
            
                
        
    
