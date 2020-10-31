x = int(input())
N = 1000 - x
array = [500,100,50,10,5,1]
cnt = 0

for coin in array:
    cnt += N // coin #cnt는 총 금액을 해당 coin으로 나눈걸 더해줌
    N %= coin

#    x = N//coin
#    N = N - coin * x
#    cnt = cnt + x

print(cnt)