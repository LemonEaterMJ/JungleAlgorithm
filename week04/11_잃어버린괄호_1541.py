#그리디 알고리즘
import sys
input = sys.stdin.readline

line = input().rstrip()

newLine = line.split('-')
# print(newLine)

result = 0
index = 0
for things in newLine : # things = 더하기로만 이뤄진 뭉텅이
    nums = list(map(int, things.split('+')))
    # sum(nums)
    if index == 0 : 
        result += sum(nums)
        index += 1
    else : 
        result -= sum(nums)
        index += 1
print(result)
    
    
        