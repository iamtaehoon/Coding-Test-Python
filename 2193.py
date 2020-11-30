#이친수 문제.
#dp(n) = dp(n-2)+ dp(n-3)+ ... + dp(1) +1 이라는 식이 나왔는데 만져보니, 피보나치 꼴로 만들어짐. --> 10 으로 시작해야 하기 때문!
#사실, 몇 개를 해보니 피보나치꼴이 나왔고 그 이유를 찾기 위해 노력했음.
#실전에서는 몇개 해보고 확인되면 그냥 바로 식 만들면 될듯.

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 1:
        return dp[x]
    dp[x] = fibo(x - 1) + fibo(x - 2)
    return dp[x]


n = int(input())
dp = [1] * (n + 1)
print(fibo(n))
