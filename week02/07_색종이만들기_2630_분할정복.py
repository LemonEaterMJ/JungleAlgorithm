import sys
from math import log2
input = sys.stdin.readline

N = int(input())
paper = []
for i in range(0, N) : 
    paper.append(list(input().split()))
# paper[y좌표 : 열][x좌표 : 행]
# print(paper)
# print(paper[0][:4])

k = round(log2(N))  # N의 지수값 k

# return : list
# k : 재귀 깊이 겸 현재 변 길이 2^k
def cutPaper(k : int, thisPaper : list) :
    # 초기 조건 설정 
    if k == 0 : #한칸 
            return [thisPaper]
    
    # 전부 같은 색인지 검사문 
    flag = 0
    temp = thisPaper[0][0]
    for horLines in thisPaper : 
        for idx in horLines : 
            if idx != temp : # 전부 같지 않음 
                flag = 1
                break
        if flag == 1 : break
    
    if flag == 0 : #thisPaper내 모든 원소는 같은색 
        #종이 자르지 않고 리턴 
        return [thisPaper]            
    
    
    newPaper_0 = []
    newPaper_1 = []
    newPaper_2 = []
    newPaper_3 = []
    for i in range(0, 4) : # 0, 1, 2, 3사분면 
        if i == 0 : #0사분면 
            for hor in range(2**(k-1)) : #가로줄 차례대로 
                newPaper_0.append(list(thisPaper[hor][:2**(k-1)]))
                # print(newPaper_0)
        elif i == 1 : 
            for hor in range(2**(k-1)) : #가로줄 차례대로 
                newPaper_1.append(list(thisPaper[hor][2**(k-1):]))
        elif i == 2 : # 2사분면 
            for hor in range(2**(k-1), 2**k) : #가로줄 차례대로 
                newPaper_2.append(list(thisPaper[hor][:2**(k-1)]))
        elif i == 3 : # 3사분면 
            for hor in range(2**(k-1), 2**k) : #가로줄 차례대로 
                newPaper_3.append(list(thisPaper[hor][2**(k-1):]))
    return cutPaper(k-1 , newPaper_0) + cutPaper(k-1 , newPaper_1) + cutPaper(k-1 , newPaper_2) +  cutPaper(k-1 , newPaper_3)          
# print(cutPaper(k, paper))

count_w = 0 #흰색종이
count_b = 0 #파란종이

for t in cutPaper(k, paper) : 
    if t[0][0] == '1' : 
        count_b += 1
    else : 
        count_w += 1
        
print(count_w)
print(count_b)      
        
    

