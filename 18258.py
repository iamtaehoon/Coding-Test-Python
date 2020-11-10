
import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline())

def pop():
    if is_empty():
        return -1
    else:
        return queue.pop()

def size():
    return len(queue)

def is_empty():
    if size() == 0:
        return 1
    else:
        return 0

def front():#나중에 들어간거
    if is_empty():
        return -1
    else:
        return queue[-1]

def back():
    if is_empty():
        return -1
    else:
        return queue[0]



for _ in range(n):

    x = sys.stdin.readline().split()
    if x[0] == 'pop':
        print(pop())
    elif x[0] == 'size':
        print(size())
    elif x[0] == 'empty':
        print(is_empty())
    elif x[0] == 'front':
        print(front())
    elif x[0] == 'back':
        print(back())
    elif x[0] == 'push':
        queue.appendleft(int(x[1]))
