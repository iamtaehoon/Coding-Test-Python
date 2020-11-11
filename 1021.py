import sys

n,m = map(int,sys.stdin.readline().split())
targets = list(map(int,sys.stdin.readline().split(' ')))
queue = [i for i in range(1,n+1)]

ans = 0
for target in targets:
    plus_index = queue.index(target)
    minus_index = len(queue) - plus_index
    steps = min(plus_index,minus_index)

    if steps == plus_index:
        sign = 'plus'
    else:
        sign = 'minus'

    if sign == 'plus':
        for _ in range(steps):
            temp = queue.pop(0)
            queue.append(temp)
    else:
        for _ in range(steps):
            temp = queue.pop(-1)
            queue.insert(0,temp)

    ans += steps
    queue.pop(0)

print(ans)
