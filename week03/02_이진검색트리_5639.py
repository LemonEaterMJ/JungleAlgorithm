# 그래프 탐색 기본 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Node : 
    def __init__(self, data) : 
        self.value = data
        self.left = None
        self.right = None
    
class bTree : 
    def __init__(self) : 
        self.root = None


tree = bTree()

def searchBTree(num : int, nowN : Node) : # 이진트리 검색 및 삽입
    if nowN.value < num : 
        if nowN.right == None : #비어있으면 삽입 
            nowN.right = Node(num)
        else : 
            searchBTree(num, nowN.right)
    else : # nowN.value > num 
        if nowN.left == None : #비어있으면 삽입 
            nowN.left = Node(num)
        else : 
            searchBTree(num, nowN.left)
    

# 입력값들을 이진트리에 입력 
while 1 : 
    try : 
        nowRoot = int(input())
    except : 
        break
    
    if tree.root == None : # 초기 루트 생성
        tree.root = Node(nowRoot)
    else : 
        searchBTree(nowRoot, tree.root)
    
def postOrder(nowNode : Node) : #left-right-root
    if nowNode.left != None : 
        postOrder(nowNode.left)
    if nowNode.right != None : 
        postOrder(nowNode.right)
    print(nowNode.value)

postOrder(tree.root)