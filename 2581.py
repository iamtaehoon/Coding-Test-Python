#맨 처음 문제를 풀 때 시간초과가 나옴,
#해결하려고 소수가 나오면, 그 소수의 2배수들을 전부 리스트에 넣어.
#num in multiple_list: 에 있으면 continue를 시켜줌. 근데 또 시간초과뜸.

# 해결책은 is_prime_num이 2 이상이 되면 어차피 소수가 아니니까 break를 시켜주는 거였음
# 간단한건데 복잡한 해결책을 생각하다가 보지 못함.
start = int(input())
end = int(input())
sum, min_prime = 0, 0

for num in range(start,end+1):

    is_prime_num = 0
    for i in range(2,num+1):
        if num%i == 0:
            is_prime_num += 1
        if is_prime_num >= 2:
            break
    if is_prime_num == 1:
        if sum == 0:
            min_prime = num
        sum += num


if sum ==0:
    print(-1)
else:
    print(sum)
    print(min_prime)
