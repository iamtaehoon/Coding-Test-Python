#몇 개 입력받을지 말하고 한 줄에 전부 입력하는 경우 list(map())....이케 가능!!!!


#ary = input().split()
#ary = list(map(int, ary)) #이걸 묶을수 없나? 바로 애초에 정수로 받는건 불가능한가?
#ary.sort(reverse = True) #이거 대신 가장 큰, 두번째로 큰만 찾는 방법도 있음

n,m,k = map(int,input().split())


ary = list(map(int, input.split()))
ary.sort(reverse = True)

v = m //(k+1)
answer = (m - v)* ary[0] +v * ary[1]
print(answer)
