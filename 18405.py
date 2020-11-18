#역시 문제를 똑바로 보지 않음 n*n 정방형인데 n*m으로 잘못보고 한참을 끙끙댐. 문제를 제대로 읽는 습관을 들여야함. 계속 같은 실수 반복
#먼저 문제를 봤을때, 바이러스들이 다 다르게 있는데 어떻게 우선순위를 구하지라는 생각을 했다.
# 생각하다보니 아예 거꾸로 생각을 해서 입력값에서부터 bfs를 해줘 가장 가까운 바이러스를 찾으려 했다.
#더 깊게 생각했어야 하는데, 그러지 못하고 문제를 풀었음.
#결과적으로 반례가 존재한다. 
# 0 0 0 0 0 0 4
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 2 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 3 0 0 0 0 0 T

#3이 가장 가깝지만 2가 막아버려서 결과적으로 가장 가까운건 4가 됨.
#짧게 생각한 이유. 신박한 아이디어라고 생각해서 순간 흥분함...

#다른 사람들의 풀이를 보고 다시 풀어보자.
# queue에 넣어두고 정렬을 하는 방법.
# 바이러스 순서대로 정렬을 해두면, 1번 바이러스들이 다 퍼지고 나서. 끝나면 2번이 이제 시작할거고. ...k번이 끝나고 나면. 다시 새로생긴 1번 애들이 순서대로 들어있을테니까 계속 queue 해주면 되는 문제

from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = []
row, len_virus = map(int,input().split())
cylinder = list()
time_array = [[0]* row for _ in range(row)]
for _ in range(row):
    cylinder.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

for i in range(row):
    for j in range(row):
        if cylinder[i][j] != 0:
            queue.append([cylinder[i][j],i,j])#큐에 넣을 때 바이러스의 종류,좌표값을 같이 넣어준다.
queue.sort()#이걸 하면 바이러스 순서대로 정렬을 할 수 있다.
queue = deque(queue) # 정렬을 하고 나서 큐에 넣는다,(큐-스택은 자료를 정렬하기에 좋은 자료구조가 아님!)

while queue:

    virus_type,virus_x,virus_y = queue.popleft()
    if time_array[virus_x][virus_y] >= s:
        break
    for i in range(4):#상하좌우로 움직여주면서
        nx = virus_x + dx[i]
        ny = virus_y + dy[i]

        if nx<0 or ny<0 or row<=nx or row <= ny:
            continue
        if cylinder[nx][ny] !=0:#갈수 있는 곳 중에서 감염 안된곳만 갈거임. 이미 감염된 곳은 갈 수 없어
            continue
        cylinder[nx][ny] = virus_type #감염!
        queue.append([virus_type,nx,ny])#감염시켰으니 그것도 1초 뒤에 다른걸 감염시켜야지. 큐에 넣어 
        time_array[nx][ny] = time_array[virus_x][virus_y]+1 #각 자리가 시간이 얼마나 걸리는지 볼 수 있음.

#print(cylinder)
#print(time_array)

print(cylinder[x-1][y-1])
