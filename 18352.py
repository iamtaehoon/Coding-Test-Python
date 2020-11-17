# 아무리 봐도 다 구현했는데, 왜 안되나 했더니 단방향이었네. 문제를 똑바로 읽자...
# 답지보고 왜 남들은 한쪽만 한거지? 생각하다 문제를 다시 읽으니 단방향이었음. 집중좀 하자
from collections import deque
import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(v,visited):
    queue = deque()
    queue.append(v)
    visited[v] = 0
    start = v
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == 0 and i != start:
                queue.append(i)
                visited[i] = visited[v] + 1


n,m,k,x = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    node1, node2 = map(int,sys.stdin.readline().split())
    graph[node1].append(node2)

#print(graph)
bfs(x,visited)
#print(visited)
is_available = False
for i in range(n):
    if visited[i+1] == k:
        print(i+1)
        is_available = True
if not is_available:
    print(-1)
