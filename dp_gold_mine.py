dx = [-1,0,1]
dy = [-1,-1,-1]

n,m = map(int,input().split())
array = []
result = [[0]*m for i in range(n)]
for i in range(n):
    array.append(list(map(int,input().split())))

for j in range(m):
    for i in range(n):
        max_num = 0
        for k in range(3):
            nx = i + dx[k]
            ny = j + dy[k]
            if j == 0:
                result[i][j] = array[i][j]
                continue
            if (nx<0) or (n<=nx) or (ny<0) or (m<=ny):
                continue
            max_num = max(max_num,result[nx][ny])
        result[i][j] = array[i][j] + max_num#앞에 3개중에 최

print(max(max(result)))

