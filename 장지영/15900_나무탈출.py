# 자식에서 루트 노드까지 가는 모든 루트의 합이 홀짝 

import sys 
input = sys.stdin.readline

N = int(input())


tree = {}
for i in range(1, N + 1) : 
    tree[i] = []

for _ in range(N - 1) : 
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)
    
