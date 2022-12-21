import sys
input = sys.stdin.readline

def find(x) : 
    if parent[x] != x : 
        parent[x] = find(parent[x])
    return parent[x]    

def union(x, y) : 
    x = find(x)
    y = find(y)
    
    if x < y : 
        parent[y] = x
    else : 
        parent[x] = y
    


N = int(input())

parent = [i for i in range(N + 1)]

for n in range (N - 2) : 
    x, y = map(int, input().split())
    union(x, y)


# 어차피 그룹은 두개밖에 없다
group1_parent = find(1)
for n in range (2, N + 1) : 
    find(n)
    if parent[n] != group1_parent : 
        print(group1_parent, parent[n])
        break
        