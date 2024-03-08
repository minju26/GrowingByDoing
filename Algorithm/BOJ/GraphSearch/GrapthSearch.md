# Graph Search (그래프 탐색)

### 정점 S가 출발지로 주어졌을 때, 이로부터 도달 가능한 곳과 경로를 찾는 것
- 그래프 내의 특정 목표 찾기
- 목적지까지의 경로가 있음을 보이기
- 목적지까지의 임의의 경로 혹은 최단 경로 찾기
- 그래프의 전반적인 연결 상태를 알아내 활용하기

### Graph
- Vertex(정점)과 Edge(간선)로 이루어진 자료구조
- 물리적 연결관계 뿐 아니라 추상적 관련성도 표현
- Directd Graph: 간선에 방향이 있는 그래프
- Undirected Graph: 간선에 방향이 없는 그래프

## DFS (깊이 우선 탐색)
    "도달할 수 있는 곳까지 최대한 깊이 탐색"

- DFS가 찾는 경로는 항상 최단 경로는 아님
- Stack(스택)을 이용해 재귀함수로 구현

```python
def DFS(graph, v, visited):
    #현재 노드 방문 표시
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)
```

## BFS (너비 우선 탐색)
    "한 번에 갈 수 있는 여러 갈래길을 동시에 넓게 탐색"

- BFS가 찾는 경로는 최소 개수의 간선을 사용하는 경로    
(모든 간선이 같은 비용인 경우에 최단 경로)
- Queue(큐)를 이용 (가까운 간선부터 우선순위)
- Python에서는 deque 라이브러리를 이용할 수 있음
```python
from collections import deque

def BFS(graph, start, visited):
    #deque로 큐 구현
    queue = deque([start])
    #현재 노드 방문 표시
    visited[start] = True

    #큐가 빌 때 까지
    while queue:
        v = queue.popleft()
        #연결된 원소 중, 아직 방문하지 않은 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append[i]
                visited[i] = True
```
