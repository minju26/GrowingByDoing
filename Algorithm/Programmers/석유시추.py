def bfs(graph, i, j):
    queue = [(i, j)]
    graph[i][j] = 0
    
    cnt = 0
    indexs = [j]
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]
    
    
    while queue:
        cnt += 1
        i, j = queue.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            if 0<= ni < len(graph) and 0 <= nj < len(graph[0]):
                if graph[ni][nj] == 1:
                    queue.append((ni, nj))
                    graph[ni][nj] = 0
                    if nj not in indexs: indexs.append(nj)
    return indexs, cnt


def solution(land):
    
    row = len(land)
    col = len(land[0])
    
    tjrdb = []
    result = [0]*col
    
    for j in range(col):
        for i in range(row):
            if land[i][j] == 1:
                indexs, cnt = bfs(land, i, j)
                tjrdb.append((cnt, indexs))
    
    for val, index in tjrdb:
        for i in index:
            result[i] += val
    
    return max(result)


# land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
# solution(land)