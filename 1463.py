#1463
#1만들기. 강의를 듣고 bfs로 풀었던 문제라 쉽다 생각했는데, bfs로 푸니 메모리 부족이 떴다.
#확실히 dp문제는 점화식을 만들어 중복되는 계산을 없애주는것이 중요하다는 것을 느낌.
#추가적으로 bfs, dfs 시간복잡도 구하는 법 알아보기!(다음에 복습할때. 30일 이후 여유 생길때)


n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1  

    if i%2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2]+1
        
    if i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1
