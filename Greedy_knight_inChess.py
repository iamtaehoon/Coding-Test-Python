# 왕실의 나이트
# 점하나에 최대 8 * 4번계산
# cnt+=1

nn = list(input())  # a5 한개씩 쪼개넣기
n = [-1,-1]

chess_row = ['1', '2', '3', '4', '5', '6', '7', '8']
chess_col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(8):
    if nn[0] == chess_col[i]:
        n[0] = i
    if nn[1] == chess_row[i]:
        n[1] = i

result = [0, 0]
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]
cnt = 0

for i in range(8):
    result[0] = n[0] + dx[i]
    result[1] = n[1] + dy[i]
    if (0 <= result[0]) and (result[0] < 8) and (0 <= result[1]) and (result[1] < 8):
        cnt += 1

print(cnt)
