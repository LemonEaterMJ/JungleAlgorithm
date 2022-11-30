import sys
input = sys.stdin.readline

# 정수를 저장하는 스택을 구현하자 
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

N = int(input())

myStack = []    
ptr = 0         # 스택 크기 및 input 위치 포인터 


for i in range(0, N) : 
    doIt = input().split()
    
    
    # if-else 로 명령어 구분 
    if doIt[0] == 'push' : 
        myStack.append(doIt[1])
        ptr += 1
    elif doIt[0] == 'pop' : 
        if ptr <= 0 : #stack 이 비어있음
            print(-1)
        else : 
            print(myStack[ptr - 1])
            del myStack[ptr - 1]
            ptr -= 1
    elif doIt[0] == 'size' : 
        print(ptr)
    elif doIt[0] == 'empty' : 
        if ptr <= 0 : 
            print(1)
        else : 
            print(0)
    elif doIt[0] == 'top' : 
        if ptr <= 0 : #stack empty
            print(-1)
        else : 
            print(myStack[ptr - 1])
        
    