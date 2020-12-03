#브루트포스로 풀 수 없음. 범위가 너무 큼.
#양수는 무조건 더하고, 음수가 나오면 더하는거랑 아예 처음부터 시작하는거 중에 뭐가 더 큰지 비교해ㅔ서 더 큰거를 넣어줌.
#예외적인 케이스로 모두 음수인 경우에는 한개는 넣어줘야 하니까 가장 큰 음수값을 넣어줌.

import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

max_num = int(-1e9)
now_num = 0
minus_cnt = 0
for i in range(len(array)):
    if array[i] >= 0:
        now_num += array[i]
    else:
        minus_cnt += 1
        now_num = max(0, now_num + array[i])

    if now_num > max_num:
        max_num = now_num
if minus_cnt == len(array):
     max_num = max(array)

print(max_num)
