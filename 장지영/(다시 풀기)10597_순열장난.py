'''
긴 문자열을 최대 50개의 숫자로 나눠야 하는게 아니다! 문제를 잘 읽자 ㅎㅎㅎㅎ 
애초에 순열이 1부터 N까지로 이뤄져 있다! 무조건 1 - N 까지 숫자는 전부 포함되어 있다. 
DFS 로 간단히 풀 수 있다. 
'''

import sys
input = sys.stdin.readline

nLine = input()


nList = []
visited = []

# 일단 순열 길이를 계산해서 N을 계산하자 
# def dfs(num, strNow) : 
    
        
        
idx = 0



print(*nList)

