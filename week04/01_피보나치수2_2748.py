# 동적 프로그래밍 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# n번째 피보나치 수를 출력하라
n = int(input())

fibonacci = []

for i in range(91) : 
    if i == 0 : 
        fibonacci.append(0)
    elif i == 1 : 
        fibonacci.append(1)
    else : 
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        
print(fibonacci[n])


# =========== 재귀 피보나치 : 메모리/시간초과 =========================

# def fibonacci(num : int) : 
#     if num == 0 : 
#         return 0
#     elif num == 1 : 
#         return 1
#     else : 
#         return fibonacci(num - 1) + fibonacci(num - 2)
    
# print(fibonacci(n))