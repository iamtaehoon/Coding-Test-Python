#브루트포스문제.
#유레카 이론
#모든 삼각수들을 리스트에 넣고
#이 리스트들을 한개한개 꺼내서 1부터 1001이 3개로 가능한가를 확인해줌. 가능하면 dp[숫자]값을 1로 바꿔줌, 기본값은 0.

import sys
input = sys.stdin.readline
samgak_num = []
num = 0
i = 1
while num <= 1000:
    num = int(i * (i + 1) / 2)
    samgak_num.append(num)
    i += 1

dp = [0]*1001
cnt = len(samgak_num)
for x in range(cnt):
    for y in range(x,cnt):
        for z in range(y,cnt):
            if samgak_num[x]+samgak_num[y]+samgak_num[z] <= 1000:
                dp[samgak_num[x]+samgak_num[y]+samgak_num[z]] = 1

T = int(input())
for _ in range(T):
    x = int(input())
    print(dp[x])
