#7
#15 11 4 8 5 2 4
#전투력 순서대로 내림차순 정리.
#어떤 경우가 최대 병사를 배치할 수 있을까?

#강의 풀이
#가장 긴 증가하는 부분수열
n = int(input())
ary = list(map(int,input().split()))
ary.reverse()

dp = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if ary[j] < ary[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(dp)
print(n - max(dp))




'''#내풀이
n = int(input())
ary = list(map(int,input().split()))
d = [0]*n
for i in range(n):
    for j in range(i+1,n):
        if ary[i]>ary[j]:
            d[i]+=1

result = 0
for i in range(n-1):
    if d[i] <= d[i+1]:#< <= 뭘까
        result += 1

print(result)
'''
