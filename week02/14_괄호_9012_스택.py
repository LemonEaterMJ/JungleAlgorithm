import sys
input = sys.stdin.readline

T = int(input())

myStack = []
ptr = 0


def isVps(data : str, dataLen : int) : 
    # 홀짝 판정 : 짝수일때만 vps
    if dataLen %2 == 1 : # odd
        return 'NO'
    else : 
        if data[0] != '(' : # (로 시작할때만 vps 
            return 'NO'
        else : 
            flag = 0 
            for onePar in data : 
                if onePar == '(' :
                    flag += 1
                else : 
                    flag -= 1
            if flag == 0 : # (와 )가 모두 짝지
                return 'YES'
            else : 
                return 'NO'
            


for i in range(0, T) : 
    vps = input().strip()   #string
    print(isVps(vps, len(vps)))