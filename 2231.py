n = input()
have_value = False

for i in range(1,int(n)):#숫자가 바뀜!
    digit = len(str(i))

    sum = i#입력 숫자만큼!
    for j in range(1,digit+1):#자리수만큼!
        sum += int(str(i)[-j])

    if sum == int(n):
        have_value = True
        print(i)
        break
    else:
        continue
if not have_value:
    print(0)
