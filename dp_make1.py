#일정한 규칙이 없음. 그래서 하나하나 모든 경우의 수를 대조해야함
#가장 빨리 1에 도착해야 하므로 1을 목적지로 생각해 최단거리를 구한다고 생각. 그러면 bfs를 사용하면 편함.
#bfs로 풀거임, cnt는 0,1,1,1,1,2,2,2,2,.. 순서대로 들어갈거니까 최단거리가 나온 순간 뒤에는 더 안해도 됨.

# 정수 x를 주면 연산의 최솟값을 출력한다.
# 연산의 종류. 5로 나누기 3으로 나누기 2로 나누기 1을 빼기

from collections import deque

x = int(input())
queue = deque()#숫자랑 몇 번 연산이 진행되었는가
queue.append((x,0))

while queue:
    num, cnt = queue.popleft()
    #종료조건 2,3,5
    if num == 2 or num == 3 or num == 5:
        cnt += 1
        break
    if (num % 5 == 0):
        queue.append((num/5,cnt+1))
    if (num % 3 == 0):
        queue.append((num/3,cnt+1))
    if (num % 2 == 0):
        queue.append((num/3,cnt+1))
    queue.append((num-1,cnt+1))

print(cnt)
