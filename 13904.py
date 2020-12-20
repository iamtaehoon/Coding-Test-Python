#13904 / 과제 문제

#알고리즘 수업 시간에 배워서 쉽게 풀 수 있었음
#비용이 제일 큰거 순서대로 정렬하고, 들어갈 수 있는 가장 늦은 시간에 넣어주기.

import sys
input = sys.stdin.readline

n = int(input())
has_homework = [False]*(1001)
input_ary = []
sum = 0
for i in range(n):
    input_ary.append(tuple(map(int,input().split())))
    sort_ary = sorted(input_ary,key = lambda x: x[1],reverse=True)
#print(sort_ary)
for i in range(n):
    duplicate_i = sort_ary[i][0]
    while True:
        if duplicate_i == 0:
            break
        if has_homework[duplicate_i] == True:#그날 이미 방이 차있다면
            duplicate_i -= 1
            continue
        #if has_homework[duplicate_i] == False:#스케쥴이 비어있는경우임.
        has_homework[duplicate_i] = True
        sum += sort_ary[i][1]
        #print(sort_ary[i][0],sort_ary[i][1])
        break
print(sum)
