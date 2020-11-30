#큰수만들기 문제. 이미 풀어봤던 문제고 쉽게 풀릴지 알았는데
#자꾸 시간초과가 남. 왜그런건지 아직도 모르겠어서 코드 참고했는데
#물어볼 곳이 없음 나중에 다시 봐보기
#1차 시도: 20/11/30

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def show_min_coin(k):
    if k == 0:
        return 0
    if dp[k] >0:
        return dp[k]
    
    minVal = 999999
    for i in range(n):
        if (k-coin_type[i]) < 0:
            continue
        minVal = min(minVal,show_min_coin(k-coin_type[i])+1)
    dp[k] = minVal
    return dp[k]

n,k = map(int,input().split())
coin_type = []
for _ in range(n):
    coin_type.append(int(input()))
dp = [0]*(k+1)

result = show_min_coin(k)
if result == 999999:
    print(-1)
else:
    print(result)




#시간초과코드
'''
    import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def show_min_coin(k):
    if k == 0:
        return 0
    if dp[k] != 999999:
        return dp[k]
    minVal = dp[k]
    for i in range(n):
        if (k-coin_type[i]) < 0:
            continue
        minVal = min(minVal,show_min_coin(k-coin_type[i])+1)
    dp[k] = minVal
    return dp[k]

n,k = map(int,input().split())
coin_type = []
for _ in range(n):
    coin_type.append(int(input()))
dp = [999999]*(k+1)

result = show_min_coin(k)
if result == 999999:
    print(-1)
else:
    print(result)
'''
