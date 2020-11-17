#소수 구하기 문제인데, 계속 시간초과 떠서 답지 보긴 함.
#소수는 제곱근까지만 돌리면 되는구나!

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

m,n = map(int, input().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)
