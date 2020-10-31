num = int(input())
ary = list()

x = input()
x = x.split()
for i in range(num):
    ary.append(int(x[i]))

ary.sort()
sum = 0

for i in range(num):
    sum = sum + ary[i] * num
    num = num - 1
print(sum)