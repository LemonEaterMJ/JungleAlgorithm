#그래프탐색 기본 
import sys
input = sys.stdin.readline


# 이진 트리 노드의 갯수 
N = int(input())

bTree = {}

for _ in range(N) : 
    mid, left, right = input().split()
    bTree[mid] = [left, right]
    # bTree[root][0]: left / [1] : right
    
    
def preorder(root : str) : # 전위순회 : root-left-right
    # 현재 노드 
    print(root, end='')
    
    left = bTree[root][0]
    right = bTree[root][1]
    
    # left 순회 
    if left != '.' : # 빈칸이 아니라면 
        preorder(left)
    if right != '.' : 
        preorder(right)
        
def inorder(root : str) : # 중위순회 : left-root-right
    left = bTree[root][0]
    right = bTree[root][1]
    
    # left 순회 
    if left != '.' :
        inorder(left)
    print(root, end='')
    if right != '.' : 
        inorder(right)
        
def postorder(root : str) : #후위순회 : left-right-root
    left = bTree[root][0]
    right = bTree[root][1]
    
    # left 순회 
    if left != '.' :
        postorder(left)
    if right != '.' : 
        postorder(right)
    print(root, end='')
    
    
preorder('A')
print()
inorder('A')
print()
postorder('A')
# print('\n')

    