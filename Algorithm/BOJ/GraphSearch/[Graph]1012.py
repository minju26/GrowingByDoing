#boj 1012 :: 유기농 배추 :: silv.2

import sys
input = sys.stdin.readline

t = int(input())
result = [0]*t

#상,하,좌,우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = [(x,y)]
    qkx[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if qkx[nx][ny] == 1:
                queue.append((nx, ny))
                qkx[nx][ny] = 0


# m:가로, n:세로, k:배추수, qkt:전체밭
for i in range(t):
    m, n, k = map(int, input().split())
    qkx = [[0]*(n) for _ in range(m)]
    cnt = 0

    for j in range(k):
        x, y = map(int, input().split())
        qkx[x][y] = 1

    for a in range(m):
        for b in range(n):
            if qkx[a][b] == 1:
                bfs(a, b)
                cnt+=1

    result[i] = cnt

for ans in result:
    print(ans)


# qkx[x][y] 와 같이 표현하려면 m을 행, n을 열로 설정해야 하는데.. 
# 단순히 가로 m, 세로 n이므로 qkx = [[0]*( m ) for _ in range( n )]으로 표현해버림.

'''
DFS로 푸는 경우 재귀를 사용해야 하는데, 파이썬의 기본 재귀 깊이 제한(100)이 있어서
코딩테스트 환경에서는 에러메세지가 뜨는 경우가 있다고 한다.
이런 경우,
    import sys
    sys.setrecursionlimit(100000)
위와 같이 재귀의 한도를 풀어줄 수 있다.
'''