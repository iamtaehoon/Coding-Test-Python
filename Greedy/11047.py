num, total_money = input().split()
CoinType = list()
num = int(num)
total_money = int(total_money)
cnt = 0

for i in range(num):
    x = int(input())
    CoinType.append(x)
CoinType.append(100000001)
while total_money != 0:
    i=0
    while total_money >= int(CoinType[i]):
        i += 1

    num_of_this_coin = total_money // int(CoinType[i-1])
    total_money = total_money - num_of_this_coin * int(CoinType[i-1])
    cnt = cnt + num_of_this_coin
    num_of_this_coin = 0

print(cnt)