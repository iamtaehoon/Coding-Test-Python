# 타일 맞추기 2
# dp 유형이 어째 다 똑같네?
# 약간 헤매긴했는데 몇 개 해보니까 금방 보임

n = int(input())
dp = [0] * (1001)
dp[1] = 1
dp[2] = 3
for i in range(3,n+1):
    dp[i] = (dp[i-1] + 2*dp[i-2])%10007


print(dp[n])
