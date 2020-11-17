#bfs를 사용해서 어떻게 구현할지는 감을 잡았는데
# bfs에서 최단경로, 최단길이를 나타내는 걸 어떻게 하는지에서 막힘.
# 다시 거꾸로 되돌아가야하나 생각 해봤지만 이 상어 문제에서 하기엔 너무 오래걸림
#아기상어 문제는 다시 저걸 해결한 이후에 도전하는걸로 -->11/17

from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n = int(input())
array = list()
visited = [[False]*n for _ in range(n)]
type_fish = [0,0,0,0,0,0,0]
num_fish = 0
shark_size =2#상어의 몸집
shark_eaten = 0#먹은 물고기의 개수 . 초기화 필요함
time = 0

for i in range(n):
    array.append(list(map(int,input().split())))
print(array)

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            #bfs
            x,y = i,j
            break

queue = deque()
queue.append([x, y])

while queue:

    where_shark = queue.popleft()
    x = where_shark[0]
    y = where_shark[1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or n <= ny or n <= nx or array[nx][ny]>shark_size:
            continue
        if array[nx][ny]<shark_size:
            array[nx][ny] = 0#물고기는 먹고
            shark_eaten += 1

            if shark_size<=shark_eaten:
                shark_eaten = 0#상어 몸집 키우고, 먹은거는 초기화
                shark_size += 1

            queue.__init__()

        queue.append([nx, ny])
