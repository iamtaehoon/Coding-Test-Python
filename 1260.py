#11.16 1차 복습. 문제 없이 성공!
# 다만 아쉬운 점은 입력될 때부터 정렬되게 할 수는 없을까?


from collections import deque

def bfs(graph,v,visited):
    queue = deque([v])
    print(v,end=' ')
    visited_bfs[v] = True # 처음 시작한 곳 방문처리

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                print(i, end=' ')
                visited_bfs[i] = True

def dfs(graph,start,visited):
    print(start,end = ' ')
    visited_dfs[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

n, m, v = map(int,input().split())

graph = [[] for i in range(n+1)]
for _ in range(m):#여기서 애초에 들어갈 때 정렬이면 효과가 더 좋을텐데... 삽입정렬식으로 구성하면 좋을텐데??
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(n+1):
    graph[i] = sorted(graph[i])
#print(graph)

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)
