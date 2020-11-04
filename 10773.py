stack = []

k= int(input())
#sum = 0 이거 해주고 pop 할때마다 pop된거 - 하는 방법도 있음
for _ in range(k):
    x = int(input())
    if x != 0:
        stack.append(x)

    else:
        stack.pop()

print(sum(stack))
