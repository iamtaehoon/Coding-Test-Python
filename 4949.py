#이거 아마 sys 해줘야할듯

while True:
    sentence = input()
    stack = []
    is_problem = False
    if sentence == '.':
        break
    else:
        for char in sentence:
            if (char == '[') or (char == '('):
                stack.append(char)

            elif char == ']':
                if not stack or stack[-1] != '[':
                    is_problem = True
                    break
                else:#정상값 '['
                    stack.pop()# [이 튕겨져 나갈듯

            elif char == ')':
                if not stack or stack[-1] != '(':
                    is_problem = True
                    break
                else:#정상값 '['
                    stack.pop()# [이 튕겨져 나갈듯

            else:#char is 평문자일때
                continue
        #stack은 비어있고 is_problem is True
        if not stack and is_problem == False:
            print('yes')
        else:
            print('no')
