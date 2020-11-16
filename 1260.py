#11.16 1차 복습. 문제 없이 성공!
# 다만 아쉬운 점은 입력될 때부터 정렬되게 할 수는 없을까?

from collections import deque


n,m,v = map(int,input().split())
#[]있어야함

graph=[]
for _ in range(n+1):
    graph.append([])
    #0 , 1~n까지 인덱스를 갖는 이차원 배열을 만들어야함
for i in range(m):#0,1,2,3,
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()
#print(graph) #이걸로 graph 만들었다!!

#dfs, bfs 순서대로 결과를 출력하세요 end = ''



#v가 시작점

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

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



visited_dfs = [False]*(n+1)
dfs(graph,v,visited_dfs)
print()
visited_bfs = [False]*(n+1)
bfs(graph,v,visited_bfs)
