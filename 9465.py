#2*N 모양의 타일에 2*1 타일을 넣는데 몇 가지 경우의 수가 가능한가
#일일히 해보니까 피보나치가 나와서 피보나치로 품.
#왜 피보나치냐 하면 예를들어 2*5 모양의 도형은 2*3에다가 ㅡ 가로작대기 두개를 넣은 경우의수 + 2*4 모형에다가 ㅣ 세로 작대기 한개 넣은 경우의 수를 더한 것과 같으니까!

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
