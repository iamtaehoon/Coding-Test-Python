#바이러스 문제. 몇 개가 연결되었는지를 세니까 이건 dfs로 구현함.
#global을 써서 풀었는데, 그거보다 callbyRefer로 푸는 방법은 없을까?

node = int(input())
edge = int(input())

def dfs(graph,start,visited):
    visited[start] = True
    global cnt_infected
    for v in graph[start]:
        if not visited[v]:
            cnt_infected += 1
            dfs(graph,v,visited)

graph = [[] for _ in range(node+1)]
for _ in range(edge):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
#정렬할 필요 없을듯. 어차피 이건 최단경로로 푸는 것도 아니고. 그냥 몇개인지만 카운트 하면 되니까. 안되면 정렬해
#print(graph)
visited = [False]*(node+1)
cnt_infected = 0
dfs(graph,1,visited)

print(cnt_infected)
