import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

# 부분수열들의 길이 array
temp = [1 for i in range(0, N)]



for i in range(0, N) : 
    for j in range(0, i) :
        if A[i] > A[j] :
            temp[i] = max(temp[i], temp[j] + 1)
            
print(max(temp))    


# sort 쓰면 안되는듯