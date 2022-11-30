# 동적프로그래밍 
# 정답 봤음 - 2차원 배열 풀이 / 2중 for문 cache 풀이 
# str1 을 기준으로 str2를 앞에서부터 한글자씩 비교한다 
# 이전까지의 최대값을 cache에 저장해 뒤로 전달해준다 (cache 는 항상 최대로 유지할 수 있다)
# str2 돌릴때마다 값이 누적되어서 최종 겹치는 최장수열이 나온다. 
import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

cntArr = [0 for i in range(len(str1))]


for indx2 in range(len(str2)) : 
    cacheMax = 0
    for indx1 in range(len(str1)) : 
        if cacheMax < cntArr[indx1] : 
            cacheMax = cntArr[indx1]
        elif str2[indx2] == str1[indx1] : # if 아니고 elif 써야함~~~ 
            cntArr[indx1] = cacheMax + 1
print(max(cntArr))
            


