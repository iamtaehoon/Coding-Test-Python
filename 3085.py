#3085 사탕 게임
#맨처음 생각의 오류. 무조건 1개 바꿔야하는데, 아무것도 안바꾼 케이스를 같이 고려함
#그리고 자꾸 마지막 i,j 범위 설정에서 에러가 떠서 그냥 다른사람거 보고 여기만 참고함. 머ㅏ리가 잘 안굴러갔음.
#브루트포스 문제로 1. 위치를 바꿔주고 2. 바꿔준 애들의 가로, 세로길이중 제일 큰 값을 저장. 가장 큰 값 계속해서 갱신.
#가장 큰값을 결과로 리턴

import sys
import copy
from collections import deque
#input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,1,-1]
n = int(input())
ary = []
for _ in range(n):
    ary.append(list(input()))
#print(ary)#DELETE

def dfs(x,y,color,arry):
    cnt= [0,0,0,0]
    real_x, real_y = x, y
    for direction in range(4):
        x,y = real_x,real_y
        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx<0 or ny<0 or n<=nx or n<=ny:
                break
            if arry[nx][ny] != color:
                break
            elif arry[nx][ny] == color:
                x,y = nx, ny
                cnt[direction] += 1

    length = max(cnt[0]+cnt[1],cnt[2]+cnt[3])+1
    return length

max_candy = int(-1e9)


#이제 한개씩 바꿀건데, 복사본을 통해서 바꾸면 됨.
for i in range(n):
    for j in range(1,n):
            ary[i][j], ary[i][j-1] = ary[i][j-1], ary[i][j]
            #print(copy_ary)
            max_candy = max(max_candy,dfs(i,j,ary[i][j],ary))
            max_candy = max(max_candy, dfs(i, j-1, ary[i][j-1],ary))
            ary[i][j], ary[i][j-1] = ary[i][j-1], ary[i][j]
for i in range(n):
    for j in range(1,n):
            ary[j][i], ary[j-1][i] = ary[j-1][i], ary[j][i]
            max_candy = max(max_candy, dfs(j,i,ary[j][i],ary))
            max_candy = max(max_candy, dfs(j-1, i, ary[j-1][i],ary))
            ary[j][i], ary[j-1][i] = ary[j-1][i], ary[j][i]

print(max_candy)
