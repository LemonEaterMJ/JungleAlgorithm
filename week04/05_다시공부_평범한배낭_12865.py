# 동적 프로그래밍 
# 배낭 알고리즘 - 2차원리스트 활용하기 
import sys
input = sys.stdin.readline

# N 물품의 수   /   K 최대무게 
N, K = map(int, input().split())    

things = [(0,0)]     # 모든 물품 무게W[0] 와 가치V[1]
for thIndx in range(1, N + 1) : 
    things.append(tuple(map(int, input().split())))


knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for thIndx in range(1, N + 1) : 
    for nowWeight in range(1, K + 1) : 
        thingW = things[thIndx][0]
        thingV = things[thIndx][1]
        
        # 3-0   배낭에 처음 넣기 전까지 현상유지 
        if thingW > nowWeight : 
            knapsack[thIndx][nowWeight] = knapsack[thIndx - 1][nowWeight]   # 이전물건, 같은무게
        else : 
            contestant1 = knapsack[thIndx - 1][nowWeight]       # 여태까지의 '이무게'의 value 최대값(보장됨)
            contestant2 = thingV + knapsack[thIndx - 1][nowWeight - thingW]     # 남은 무게의 최대값
            knapsack[thIndx][nowWeight] = max(contestant1, contestant2)         # 3-1, 3-2 경합 후 최대값 이어짐

print(knapsack[N][K])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 1) x축엔 가방 1~K 까지의 무게, y축은 물건 N개 개수 만큼의 배열을 만들어준다.

# 2) 행을 차례대로 돌며 다음과 같은 알고리즘을 수행해준다.

 

# 3-0) 현재 물건이 현재 돌고있는 무게보다 작다면 바로 [이전 물건][같은 무게] (knapsack[i-1][j]를 입력해준다.
#      이렇게 되면 첫 입력 때 자신의 무게를 입력할 수 있다

# 3-1) 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값(knapsack[i-1][j-weight]을 위의 행에서 가져와 더해준다.

# 3-2) 현재 물건을 넣어주는 것보다. 다른 물건들로 채우는 값(knapsack[i-1][j])을 가져온다.

# 4) 3-1과 3-2 중 더 큰 값을 knapsack[i][j]에 저장해준다. 이 값은 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성이다.

# 5) knapsack[N][K]는 곧, K무게일 때의 최댓값을 가리킨다.

# 
# 결국 수식으로 표현하면 다음과 같다.

# knapsack[i][j] = max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])

# knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])


# 물건을 하나씩 검사할 때 최대값을 내려주기때문에, 지금물건을 넣고 남은무게를 검사할 때 앞선것들을 전부 검사할 필요 없이 
# 이전물건 상태일 때 최대값임을 보장할 수 있다 (따라서 한개만 비교한다)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 무게순으로 하나, 가치순으로 하나 정렬해서 최종값 비교하는 방법 - 오답 

    
# wThings = sorted(things, key= lambda x : x[0])      # 무게 작은순 정렬
# vThings = sorted(things, key= lambda x : -x[1])      # 가치 큰순 정렬

# # 무게 작은순으로 챙기기
# weight1 = 0
# value1 = 0
# for wIndx in range(len(wThings)) : 
#     if weight1 + wThings[wIndx][0] <= K : 
#         # 배낭에 추가 
#         weight1 += wThings[wIndx][0]
#         value1 += wThings[wIndx][1]
#     else : 
#         break
# # print(value1)


# # 가치 큰순으로 챙기기
# weight2 = 0
# value2 = 0
# for vIndx in range(len(vThings)) : 
#     if weight2 + vThings[vIndx][0] <= K : 
#         # 배낭에 추가 
#         weight2 += vThings[vIndx][0]
#         value2 += vThings[vIndx][1]
#     else : 
#         break
# # print(value2)

# print(max(value1, value2))
