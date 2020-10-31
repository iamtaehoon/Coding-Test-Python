x = input()
minus_ary = list()
minus_ary = x.split("-")

y = 0
for i in range(len(minus_ary)):
    sum = 0
    plus_ary = minus_ary[i].split("+")

    for j in plus_ary:
        sum = sum + int(j)

    minus_ary[i] = sum
    y = y - minus_ary[i]

y = y + 2 * minus_ary[0]
print(y)