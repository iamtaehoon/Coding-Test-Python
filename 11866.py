from collections import deque
n,k = map(int,input().split())
queue = deque()
result = []

for i in range(1,n+1):
    queue.appendleft(i)
while len(queue) != 0:
    for j in range(k-1):
        queue.appendleft(queue.pop())
    result.append(queue.pop())

print('<', end='')
for i in range(len(result)-1):
    print(result[i],end = ', ')
print(str(result[len(result)-1])+'>')
