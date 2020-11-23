#시간복잡도가 n**2인 다익스트라.
#가장 간단한 형식의 다익스트라. 대신 시간복잡도가 높음. 정렬 중 버블정렬 이런 느낌이라 보면 됨.
#좀 해멨는데, 계속 리스트가 범위를 벗어낫다고 함. 그 이유는 visited, distance를 []로 묶어버려 1개로 처리되고 있었음

import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int,input().split())
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))#왜 튜플로 항상 넣는거지. 바꿀 필요가 없으니까? 튜플이 더 장점이 있는걸까???D

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]#j[0]은 노드 j[1]은 거리 distance[노드번호] = 거리 입력 #무한대를 입력값으로 바꿔줌
    for i in range(n-1):#시작노드 빼고 총 n-1번 돌거다.
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = j[1] + distance[now]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
for i in range(1,n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
