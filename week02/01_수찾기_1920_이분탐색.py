import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())



def binSearch(N : int, A : list, numM : int) : 
    start = 0
    end = N - 1
    while start <= end : #start end pointer가 자리 바뀔때까지
        mid = (start + end) // 2
        if A[mid] == numM : # 찾았다!
            return 1
        elif A[mid] > numM : # 범위를 작게하자 
            end = mid - 1
        else : #범위를 크게하자 
            start = mid + 1
    return 0    # 없다!

for numM in list(map(int, input().split())) : 
    print(binSearch(N, A, numM))