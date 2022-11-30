# 동적 프로그래밍
import sys
input = sys.stdin.readline

# 타일 종류 : 00타일 / 1타일

N = int(input())

# N 일때의 조합 개수는 
# N-1 인 것들 앞에 1 붙이고 
# N-2 인 것들 앞에 00 붙이고 
# f(n) = f(n-1) + f(n-2)
# 피보나치 

fibo = [0] * (N + 1)

for i in range(1, N + 1) : 
    if i == 1 : 
        fibo[1] = 1
    elif i == 2 : 
        fibo[2] = 2
    else : 
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 15746   
        # 어차피 나머지를 출력하기때문에 15746 위는 계산하지 않아도 된다!

print(fibo[N])
       
        
 


