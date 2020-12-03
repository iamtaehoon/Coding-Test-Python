#9개중 7개를 순열? 조합? 해서 거기 뽑힌걸 바탕으로 7개의 합을 구함.
#break를 안해줌. break 안하면 답을 찾아도 계속해서 난쟁이들의 조합을 찾을거고, 답이 3개인 경우 3개가 나와버리겠지?
#다음번엔 답을 찾으면 한번 중간과정들 다 봐보기

import sys
from itertools import combinations

idx = [0,1,2,3,4,5,6,7,8]
input = sys.stdin.readline
idx_array = list(combinations(idx,7))

ary = [0]*9
for i in range(9):
    ary[i] = int(input())

for a,b,c,d,e,f,g in idx_array:
    #print(a,b,c,d,e,f,g)
    sum = ary[a] + ary[b] + ary[c] + ary[d] + ary[e] + ary[f] + ary[g]
    if sum == 100:#정답일 경우
        result_ary = [ary[a],ary[b],ary[c],ary[d],ary[e],ary[f],ary[g]]
        result_ary.sort()
        for x in result_ary:
            print(x)
        break


