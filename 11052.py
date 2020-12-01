#카드 구매하는 문제인데 딱맞게 구입해야 하고 제일 비싸게 사야함

#범위를 보니까 이중 포문으로 풀어야겠다 생각했음.
#바텀업 방식으로 한개한개씩 최대값 저장해주면서 풀었음. 

n= int(input())
price = list(map(int,input().split()))#price[0]을 0으로 못추가하나
dp = [0]*1001
#max값 찾아야함

for i in range(len(price)):
    dp[i+1] = price[i]

for i in range(1,len(price)+1):
    max_num = -1
    for j in range(i//2+1):
        max_num = max(dp[j]+dp[i-j], max_num)
    dp[i] = max_num
print(dp[n])
