#부분수열의 합 문제
#경우의 수가 백만이라 브루트 포스 사용

import sys
input = sys.stdin.readline
def dfs(idx, sum):
    global cnt
    if idx >= n:#인덱스 값을 벗어나는 경우
        return
    sum += ary[idx]
    if sum == s:#이미 먼저 더해주고 나서 상태를 체크해주기 때문에 모두 포함 안된 경우는 고려하지 않음
        cnt += 1
    dfs(idx + 1, sum - ary[idx])#지금 원소 포함 안한 경우
    dfs(idx + 1, sum)#포함한 경우 이렇게 두개로 나눠서 계속 진행하면 트리모양으로 그려지겠지
n, s = map(int, input().split())
ary = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
