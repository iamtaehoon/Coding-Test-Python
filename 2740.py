#2740 이건 그냥 쉬운문제. n^3도 충분히 돌아갈 수 있는 범위라 3중 반복문 사용.
#복습 필요 없음

n,m = map(int,input().split())
first = [0]*n
for i in range(n):
	first[i] = list(map(int,input().split()))
m,k = map(int,input().split())
second = [0]*m
for i in range(m):
	second[i] = list(map(int,input().split()))
ary = [[0]*k for _ in range(n)]
for i in range(n):
	for j in range(k):
		for x in range(m):
			ary[i][j] += first[i][x]*second[x][j]
for i in range(n):
	for j in range(k):
		print(ary[i][j],end=' ')
	print('')
