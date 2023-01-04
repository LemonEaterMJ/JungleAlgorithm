import sys
input = sys.stdin.readline

def merge(fileList, K) : 
    # dp[i][j]는 i번째 - j번째 파일을 합치는 최소값 
    dp = [[0] * (K + 1) for _ in range(K + 1)]
    
    # 두 파일이 연속되어있을 때의 합을 구하는 경우만 dp에 저장 
    for i in range(1, K + 1) : 
        for j in range(1, K + 1) : 
            if j == i + 1 : 
                dp[i][j] = fileList[i] + fileList[j]
    
    # dp 맨 아래부터 위로 올라오면서 dp 채우기 
    # dp[1][4] 는 dp[1][1] + dp[2][4], dp[1][2]



T = int(input())

for tc in range(T) : 
    K = int(input())
    filesizeList = [0] + list(map(int, input().split()))    # K + 1 개 
    merge(filesizeList, K)