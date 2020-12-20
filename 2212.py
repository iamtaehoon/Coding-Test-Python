#2212 센서 문제 / 그리디, 직선들에 점을 찍고 각 점 사이의 거리를 계산
#센서와 센서 사이에 기지국이 있을 경우, 그 기지국의 수신 가능영역은 직선의 길이와 동일.
#기지국이 1개일 경우에는 수신가능영역이 맨 처음에 있는 센서랑 끝에 있는 센서까지 거리가 되어야겠지?
#기지국이 2개가 된 경우에는 두 점 사이의 거리가 가장 먼거를 빼주면 됨., 기존에 1 묶음이었던 걸 2개의 묶음으로 나눠주는 개념
#한개씩 한개씩 빼나가주면 됨! 메모이제이션, 그리디 섞인 문제

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
ary = list(map(int, input().split()))
ary.sort()
new_ary = [0]*20000
for i in range(n - 1):
    new_ary[i] = ary[i + 1] - ary[i]
new_ary.sort(reverse=True)

sum = 0
for i in range(-1 + k, 20000):
    sum += new_ary[i]
print(sum)
