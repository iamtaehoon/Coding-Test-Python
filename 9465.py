#스티커 떼서 최대 점수를 만드는 문제

#점화식을 만들어서 풀 수 있었음!
#위아래를 독립으로 보고, dp[i][j] = max(왼대각선의 최대 + 현재 스티커의 점수, 왼쪽의 최대)로 하고
#지막에 위의 스티커, 아래의 스티커 중 뭐가 더 높은 점수를 갖는지 비교해서 최대값을 도출함.

t = int(input())
for _ in range(t):
    n = int(input())
    array = []
    dp = [[0 for _ in range(n)] for _ in range(2)]
    for i in range(2):
        array.append(list(map(int,input().split())))

    dp[0][0] = array[0][0]
    dp[1][0] = array[1][0]

    for j in range(1,n):
        for i in range(2):
            if i == 0:
                dp[0][j] = max(dp[1][j-1]+array[0][j],dp[0][j-1])
            else:
                dp[1][j] = max(dp[0][j-1]+array[1][j],dp[1][j-1])
    result = max(dp[0][n-1],dp[1][n-1])
    print(result)
