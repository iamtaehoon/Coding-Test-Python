n = int(input())
array = list(map(int,input().split()))
cnt = 0

for i in range(n):
    is_prime_cnt = 0
    if(array[i] == 1):
        continue
    for j in range(2,array[i]+1):
        if(array[i]%j==0):
            is_prime_cnt += 1
    if(is_prime_cnt == 1):
        cnt +=1
print(cnt)
