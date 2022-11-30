import sys
input = sys.stdin.readline

K = int(input())

myStack = []
ptr = 0

for i in range(0, K) : 
    num = int(input())
    
    # 0인지 아닌지 판단한다 
    if num == 0 : 
        del myStack[ptr-1]
        ptr -= 1
    else : 
        myStack.append(num)
        ptr += 1
    
print(sum(myStack))