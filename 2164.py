from collections import deque
n=int(input())
queue = deque()

for i in range(1,n+1):
    queue.appendleft(i)

while True:
    if len(queue) >2:
        queue.pop()
        queue.appendleft(queue.pop())
    elif len(queue) == 2:
        queue.pop()
    elif len(queue) == 1:
        print(queue[0])
        break
