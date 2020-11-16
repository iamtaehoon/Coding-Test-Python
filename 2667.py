#단지번호 붙이기 문제
#어렵지는 않았음. 오히려 dfs보다 시뮬레이션의 느낌이라 구현하는데 시간이 좀 걸림.
#global 변수를 사용할 때 어디다가 사용해야 하는거지? 그리고 global 말고 다른 방법은 어케 했는지 찾아보기


dx = [0,-1,0,1]#동북서남
dy = [1,0,-1,0]

def dfs(array,x,y,n,visited):
    visited[x][y] = True
    global apart_cnt
    apart_cnt +=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or ny<0 or n<=nx or n<=ny or array[nx][ny] != str(1):
            continue

        if not visited[nx][ny]:
            dfs(array,nx,ny,n,visited)
    #이동한 거리가 지도 안에 있고 그리고 방문한적 없고 그리고 집인 경우(1인 경우):
    #만약 이동할 수 있으면 이동시키고 dfs 실행
    #카운트 해야함./ global 해서 안에 1개



n = int(input())
array_map = [[] for _ in range(n)]
for i in range(n):
    array_map[i] = list(input())
visited = [[False]*n for _ in range(n)]

apart_set_cnt = 0 #아파트 단지의 개수, 가장 위에서 세줘야하겠지?
global apart_cnt
apart_cnt = 0 #단지 내 아파트의 개수 초기화가 필요

apart_list = []#아파트 개수들을 저장해 줄 리스트

for i in range(n):
    for j in range(n):
        if (array_map[i][j] == str(1)) and (visited[i][j] == False):#아파트가 있고 방문하지 않은 곳이면, dfs를 실행해 줌.
            dfs(array_map,i,j,n,visited)
            apart_set_cnt +=1# dfs가 끝나는 그 지점에서 아파트 단지 하나를 다 센거니까. 여기서 단지의 개수를 세 줌
            apart_list.append(apart_cnt)#그리고 그 아파트 단지 내 아파트가 몇 개 있는지 카운트 해주고 그 다음 0으로 초기화해서 다음걸 준비
            apart_cnt = 0

apart_list.sort()
print(apart_set_cnt)
for x in apart_list:
    print(x)
