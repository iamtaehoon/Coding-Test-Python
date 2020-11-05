from collections import deque

def bfs(graph,start,visited):#bfs는 while을 사용해서 빌때까지 반복하기. 1 붙어있는 2 3 8, 2처리하면 3 8 + [(1애는 visited), 7]#2에 부ㅡㅌ어있던 애들
    queue = deque([start])#bfs는 큐로 구현함. 그래서 import
    visited[start] = True

    while queue: #큐 안에 뭐가 있을때. 빌때까지 반복할거
        v = queue.popleft()#queue에서 가장 먼저 들어온애 빼주고, 거기에 붙어있는 graph[v]들 싹 다 넣을거임.
        print(v,end=' ')

        for i in graph[v]: #1에 붙어있는 애들
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph_bfs = [
    [],#첫 칸은 비워주는거임. 이 그래프라는 리스트: 인덱스 - 해당 spot, 리스트 안 숫자들 - 연결된 spot
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]
visited = [False]*9
bfs(graph_bfs,1,visited)
print()




#dfs by Python
def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


graph = [
    [],#첫 칸은 비워주는거임. 이 그래프라는 리스트: 인덱스 - 해당 spot, 리스트 안 숫자들 - 연결된 spot
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

visited = [False]*9

dfs(graph,1,visited)
