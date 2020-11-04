#1.rstrip이 머냐
# 2. 한번에 맞춰야 하는데 어떤 상황에서 readline을 해주는지, 그리고 정확한 사용법이 어떤지 알아보기

import sys


stack = []

input = sys.stdin.readline
n= int(input())

def push(x):
    stack.append(x)

def pop():
    if not empty():
        return stack.pop()
    else:
        return -1

def top():
    if not empty():
        return stack[len(stack)-1]
    else:
        return -1

def size():
    return len(stack)

def empty():
    if size() == 0:
        return 1
    else:
        return 0

for _ in range(n):
    x = input().rstrip()

    if (x == 'top'):
        print(top())
    elif (x == 'pop'):
        print(pop())
    elif (x == 'size'):
        print(size())
    elif (x == 'empty'):
        print(empty())

    else:
        a, b = x.split()
        if a == 'push':
            push(b)
