# boj 1931 :: 회의실 배정 :: silv.1

import sys

input = sys.stdin.readline

n = int(input())

timeList = []
answer = []

for _ in range(n):
    s, e = map(int, input().split())
    timeList.append((s, e))

timeList.sort(key= lambda x: (x[1], x[0]))
answer.append(timeList[0])

j = 0

for i in range(1, n):
    end = answer[j][1]
    if timeList[i][0] >= end:
        answer.append(timeList[i])
        j += 1

print(len(answer))

# 틀렸습니다 : (4, 5), (5, 5)와 같이 회의의 종료시간이 같지만 시작 < 종료,  시작==종료 인 경우 시작이 빠른 것을 먼저 선택하는 것이 이득이다. 
#   (시작 시간에 대한 정렬도 필요했음 -> timeList.sort(key= lambda x: (x[1], x[0])) )