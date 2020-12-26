#어디서 오류가 났는지 도저히 모르겟음. 더 실력을 키우고 풀어보기 4시간은 붙들고 있었는데 계속 조금씩 틀림.,.

import sys
input = sys.stdin.readline

n,m = map(int,input().split())#세로, 가로
ary = []
cnt_cctv = 0
min_num = int(1e9)
cctv_info = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def see(cctv_type,x,y,direction):
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0<=nx and nx< n and 0<=ny and ny< m:#list 인덱스 벗어남 뜨면 나눠버리기#다시 해야겠다. 9인 경우도 들어갈 수 있음.

        if ary[nx][ny] == 6:
            return
        if ary[nx][ny] == 1 or ary[nx][ny] == 2 or ary[nx][ny] == 3 or ary[nx][ny] == 4 or ary[nx][ny] == 5:
            nx += dx[direction]
            ny += dy[direction]
            if 0 <= nx and nx < n and 0 <= ny and ny < m:  # list 인덱스 벗어남 뜨면 나눠버리기#다시 해야겠다. 9인 경우도 들어갈 수 있음.
                see(cctv_type,nx-dx[direction],ny-dy[direction],direction)
                return
            else:
                return
        # (ary[nx][ny] == 0 or ary[nx][ny] == 9):
        if cctv_type == 1:
            ary[nx][ny] = 9
            see(cctv_type,nx,ny,direction)
            #여기 이후부터는 코드 다시 짜야할듯. 그냥 cctv마다 코드를 다르게 짜기

        elif cctv_type == 2:
            ary[nx][ny] = 9
            see(1,nx,ny,direction)
            nx2 = x - dx[direction]
            ny2 = y - dy[direction]
            if 0 <= nx2 and nx2 < n and 0 <= ny2 and ny2 < m:
                see(1,x,y,(direction+2)%4)

        elif cctv_type == 3:
            ary[nx][ny] = 9
            see(1,nx,ny,direction)
            nx2 = x + dx[(direction+1)%4]
            ny2 = y + dy[(direction+1)%4]
            if 0 <= nx2 and nx2 < n and 0 <= ny2 and ny2 < m:
                see(1,x,y,(direction+1)%4)

        elif cctv_type == 4:
            ary[nx][ny] = 9
            see(1,nx,ny,direction)
            nx2 = x - dx[direction]
            ny2 = y - dy[direction]
            nx3 = x + dx[(direction+1)%4]
            ny3 = y + dy[(direction+1)%4]
            if 0 <= nx2 and nx2 < n and 0 <= ny2 and ny2 < m:
                see(1,x,y,(direction+2)%4)
            if 0 <= nx3 and nx3 < n and 0 <= ny3 and ny3 < m:
                see(1,x,y,(direction+1)%4)

        elif cctv_type == 5:
            ary[nx][ny] = 9
            see(1,nx,ny,direction)
            nx2 = x - dx[direction]
            ny2 = y - dy[direction]
            nx3 = x + dx[(direction+1)%4]
            ny3 = y + dy[(direction+1)%4]
            nx4 = x + dx[(direction+3)%4]
            ny4 = y + dy[(direction+3)%4]
            if 0 <= nx2 and nx2 < n and 0 <= ny2 and ny2 < m:
                see(1,x,y,(direction+2)%4)
            if 0 <= nx3 and nx3 < n and 0 <= ny3 and ny3 < m:
                see(1,x,y,(direction+1)%4)
            if 0 <= nx4 and nx4 < n and 0 <= ny4 and ny4 < m:
                see(1,x,y,(direction+3)%4)


for i in range(n):
    ary.append(list(map(int,input().split())))
    for j in range(m):
        if ary[i][j] != 0 and ary[i][j] != 6:
            cctv_info.append([ary[i][j],i,j])#인덱스가 cctv의 번호
            cnt_cctv += 1


cctv_direction = [0]*cnt_cctv#cctv 인덱스에다가 0,1,2,3 방향을 기록해주느거
# 17 대신 이게 들어가야 하는거임!
for i in range(4**(cnt_cctv)):
    cnt = 0
    while i != 0:
        cctv_direction[cnt] = i%4
        i //= 4
        cnt += 1
    #print('cctv_direction',cctv_direction)#cctv가 바라보고 있는 방향들의 경우의 수, i가 바뀌면 cctv 방향이 1개는 바뀜. 다른 경우의 수.

    #cctv 한개씩 가져오기
    for cctv in range(cnt_cctv):

        # 바라보는 방향을 확인해서 0-->9로 바꿔주기 이제 여기는 단순구현.
        see(cctv_info[cctv][0],cctv_info[cctv][1],cctv_info[cctv][2],cctv_direction[cctv])#각 cctv 가 바라보는 방향을 확인하는것.
        # 구현이후 0개수 세주기
    cnt_sagak = 0
    #print(ary)
    for x in range(n):
        for y in range(m):
            if ary[x][y] == 0:
                cnt_sagak += 1

    #print("cnt_sagak",cnt_sagak)
    if min_num>cnt_sagak:
        min_num = cnt_sagak

    for x in range(n):
        for y in range(m):
            if ary[x][y] == 9:
                ary[x][y] = 0

print(min_num)
    #구현이후 0개수 세주기
    #0개수랑 최소값 비교해서 최소값 갱신해주
