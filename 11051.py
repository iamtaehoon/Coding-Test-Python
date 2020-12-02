#이런건 이항정리 공식을 알아야지
#nCk = (n-1)C(k-1) + (n-1)Ck
#이항정리 2

n,k=map(int,input().split())

dp = [[0]*(n+1) for _ in range(n+1)]
dp[1][0] = 1
dp[1][1] = 1
for i in range(2,n+1):
    dp[i][0] = 1
    for j in range(1, i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%10007
print(dp[n][k])

