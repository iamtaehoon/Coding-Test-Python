n =int(input())
ary = []
for _ in range(n):
    ary.append(list(map(int, input().split())))
#ary[][0]몸무게  ary[][1]키
result = []
for i in range(len(ary)):#나임
    grade = 1
    for j in range(0,len(ary)):
        if ary[i][0] < ary[j][0]:
            if ary[i][1] < ary[j][1]:
                grade += 1
    result.append(grade)

for elem in result:
    print(elem,end = ' ')
