'''
bfs 돌린다
메모리 초과가 납니다 ㅠㅜㅠ
'''

import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
board = [[0]*(k) for _ in range(k)]
count = 0

queue = deque([(0,0)])

for row in range(k):
    board[row] = list(map(int, input().split()))

def find(row, col):
    global count
    if row == k-1 and col == k-1:
        count+=1
        return
    if row>=k or col>=k:
        return
    num = board[row][col]

    if (0<=row+num<k):
        queue.append((row+num, col))
    if (0<=col+num<k):
        queue.append((row, col+num))

while(queue):
    row, col = queue.popleft()
    find(row, col)

print(count)

