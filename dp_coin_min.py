#역시나 최단거리찾기라 생각하고 bfs로 풀었음. dp로 하는거 그대로 따라하고 코드 여기 기

from collections import deque

n,m = map(int,input().split())
coin_type = []
for _ in range(n):
    coin_type.append(int(input()))
coin_type.sort(reverse=True)
queue = deque()
queue.append((m,0))
while queue:
    money, cnt = queue.popleft()
    for i in range(len(coin_type)):
        x = money - coin_type[i]
        y = cnt + 1
        if x == 0:
            cnt = y
            queue.clear()
            break
        if x < 0:
            continue
        queue.append((x,y))
if x<0:
    print(-1)
else:
    print(cnt)
