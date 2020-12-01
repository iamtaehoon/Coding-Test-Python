#제곱수의 합을 구하는데, 제곱수를 최대한 조금 써보자는 문제

#맨처음에 틀림. 32같은 경우는 16 16 해서 2가 최대인데,
# 그냥 별생각 ㅇ못하고 25+7이라는 방식으로 품.
# 많은 경우에수를 고려했어야 하나. 점화식을 잘못 만들었다고 볼 수 있음.

# 그리고 그 다음에 하니까 시간초과. 이건 내가 충분히 생각할 수 있었는데 백준이라 그냥 안일했음.
# 그래서 제곱수들만 반복해주니까 풀림.
#코드 손질 한번 해야겠다.

n = int(input())
dp = [0]*(n+1)
dp[1] = 1
for i in range(2,n+1):
	nearest_square = int((i)**0.5)
	#루트에 int 씌우면 가장 가까운 값이 나오지 않을까
	if i == nearest_square**2:
		dp[i] =1
	else:
		min_num = int(1e9)
		for j in range(1,nearest_square+1):
			min_num = min(min_num,dp[j**2]+dp[i-j**2])
		dp[i] = min_num

print(dp[n])
