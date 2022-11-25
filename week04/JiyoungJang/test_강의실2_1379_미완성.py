import sys
input = sys.stdin.readline

# 강의 개수 N 
N = int(input())

classes = [[0, 0, 0]]

for n in range(1, N + 1) : 
    classes.append(list(map(int, input().split())))

# 시작시간이 빠른 순으로 정렬
# 시작시간이 같다면 빨리 끝나는 순으로 정렬     
classes.sort(key = lambda x : (x[1], x[2]))
print(classes)

cntRoom = 1

# [교실index] = endTime
classrooms = [[0, 0], [1, 0]]

for i in range(1, N + 1) : 
    classN = classes[i][0]
    startTime = classes[i][1]
    endTime = classes[i][2]
    
    for rr in range(1, cntRoom + 1) :  
        if startTime > classrooms[rr][1] : 
            # 이 교실에서 현재 강의를 시작할 수 있음! 
            # 교실 개수는 그대로 둔다 
            # 이 교실의 강의종료시각만 갱신 
            classrooms[rr][1] = endTime
            
            # 강의에 교실을 배정해준다 
            classes[i].append(classrooms[rr][0])
            
            # 교실을 구했으니 빠져나온다 
            break
    # 전부 다 돌았는데 남는 교실이 없다 
    # 교실 한개 새로 개방 후 배정
    cntRoom += 1
    classrooms[cntRoom][1] = endTime
    classes[i].append(classrooms[cntRoom][0])
    
    # classroom 을 끝나는 시각 순으로 정렬해야할 것 같은데... 
    
print(cntRoom)
for j in range(1, N + 1) : 
    print(classes[j][3])
             
            
        
    