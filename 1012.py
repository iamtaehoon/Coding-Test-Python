#파이썬의 기본 재귀는 1000. 나중에 이런 문제가 나오면 몇번이나 재귀를 쓰는지 대충 계산해서 알맞은 재귀값을 넣어주자

import sys
sys.setrecursionlimit(100000)

def dfs(farm,x,y,visited):
    visited[x][y] = True
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if (nx<0) or (ny<0) or (row<=nx) or (col<=ny):
            continue
        if farm[nx][ny] == 1:
            if not visited[nx][ny]:
                dfs(farm,nx,ny,visited)


dx = [1,-1,0,0]
dy = [0,0,1,-1]

t = int(input())

for _ in range(t):
    col, row, k = map(int,input().split())#가로 세
    cnt = 0
    farm = [[0]*col for _ in range(row)]
    visited = [[False]*col for _ in range(row)]
    for _ in range(k):
        y,x = map(int,input().split())
        farm[x][y] = 1
    for i in range(row):
        for j in range(col):
            if farm[i][j] == 1:
                if not visited[i][j]:
                    cnt += 1
                    dfs(farm,i,j,visited)
    print(cnt)
#    print(farm)
#   print(visited)
