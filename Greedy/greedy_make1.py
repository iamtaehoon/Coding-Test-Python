#1이될때까지 문제
#n이 100000, k= 100000 최대값이라 했을때, nk가 시간복잡도라면 안되겠지?
N = int(input())
K = int(input())

#최적화 안이뤄짐
cnt = 0
#여기서 n,k가 이상한 값일때 에러메세지 띄우는거 해줘야
while(N>1): #n이 1보다 클때만 돌아감
    if (N%K==0):
        N/=K
        cnt= cnt+ 1
    else:
        N -= 1
        cnt = cnt + 1
print(cnt)




'''
#최적화o 나동빈쓰 풀이
result = 0
while True:
    target = (N//K)*K
    result += (N - target)

    N = target
    if N<K:
        break
    else:
        N//=k
        result += 1
result += (N-1)
print(result)
'''
