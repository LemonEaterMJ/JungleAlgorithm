# 그리디 알고리즘 
import sys
input = sys.stdin.readline

T = int(input())        # 테스트 케이스 개수 

for t in range(T) : 
    N = int(input())    # 지원자 숫자 
    
    people = []
    for n in range(N) : 
        people.append(tuple(map(int, input().split())))

    # 서류 순서대로 정렬하기 
    people.sort(key=lambda x : x[0])
    # print(people)
    
    count = N
    youMustWin = N + 1     # 면접 꼴찌
    for n in range(N) : 
        if n == 0 : 
            youMustWin = people[n][1]
        elif youMustWin > people[n][1] : 
            youMustWin = people[n][1]
        else : 
            # 현재 면접자 탈락 
            count -= 1
    print(count)        
            
            