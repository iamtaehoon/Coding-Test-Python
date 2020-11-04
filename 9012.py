t = int(input())

for _ in range(t):
    stack = []

    x = input()
    for i in range(len(x)):
        if x[i] == '(':
            stack.append("(")
        elif x[i] == ')':
            if len(stack) == 0:#비어있을때
                stack.append(')')
                break
            else:
                stack.pop()

    if len(stack) != 0:#stack안에 뭐 있나 없나로 검사할 수도 있나?
        print("NO")
    else:#스택 안에 아무것도 없다.
        print("YES")
    #stack초기화
    del stack  #
