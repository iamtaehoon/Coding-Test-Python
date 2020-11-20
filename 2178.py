#미로 최단거리 찾기 문제 #쉬움

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
array = []
visited = [[0]*m for _ in range(n)]
for _ in range(n):
    array.append(list(map(int,input())))

queue = deque()#n-1,m-1 들어가야함
queue.append((0,0))
visited[0][0] = 1
while queue:
    x,y = queue.popleft()
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx<0 or ny<0 or n<=nx or m<=ny:
            continue
        if array[nx][ny] == 1:
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
                #print((nx,ny))
                if (nx == n-1) and (ny == m-1):
                    print(visited[nx][ny])
                    queue.clear()
                    break
