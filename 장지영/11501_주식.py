import sys
input = sys.stdin.readline
    

def jonbuh_end(curr_list, N) :
    idx = 0
    money = 0
    maxvalue = max(curr_list)
    for n in range(N) : 
        if (curr_list[n] < maxvalue) : 
            money += maxvalue - curr_list[n]
            
        else :  
            if (n < N - 1) : 
                maxvalue = max(curr_list[n + 1:])
                idx = n + 1
    
    return money  
                                   
    


T = int(input())

for t in range(T) : 
    N = int(input())    # 날의 수 
    
    upDown = list(map(int, input().split()))
    
    print(jonbuh_end(upDown, N))
        