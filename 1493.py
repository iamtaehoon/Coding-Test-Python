#생각하는거는 금방 생각했는데 구현하는데 오래걸림
#코드가 너무 복잡. 내일 다시 코드 깔끔하게 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

dp = [0]*(20)
def cnt_qube(length,width,height):#3개중 한개만 1이어도 끝남

    if length == 1 or width == 1 or height == 1:
        dp[0] += length * width * height
        return
    if length == 0 or width == 0 or height == 0:
        return

    chasu = 0
    x = 1

    while (x <= min(length,width,height)):
        x *= 2#여기서 나온 x가 들어갈 수 있는 최대 큐브의 크기
        chasu += 1#2의 몇승인지 써놓으려고
    x/=2
    x = int(x)
    chasu -= 1

    #print(x,chasu)
    #x랑 몇개인지 기록해야함.
    cnt_length = length//x
    cnt_width = width//x
    cnt_height = height//x

    cnt_x_size = cnt_width * cnt_length * cnt_height
    dp[chasu] += cnt_x_size

    namuji_length = length - cnt_length * x
    namuji_width = width - cnt_width * x
    namuji_height = height - cnt_height * x

    cnt_qube(namuji_length,cnt_width * x,cnt_height * x)
    cnt_qube(cnt_length * x, namuji_width,cnt_height * x)
    cnt_qube(cnt_length * x, cnt_width * x, namuji_height)
    cnt_qube(namuji_length, namuji_width, cnt_height * x)
    cnt_qube(namuji_length, cnt_width * x, namuji_height)
    cnt_qube(cnt_length * x, namuji_width, namuji_height)
    cnt_qube(namuji_length, namuji_width, namuji_height)


ans = 0
length,width,height = map(int,input().split())
n = int(input())
ary = []
for i in range(n):
    ary.append(list(map(int, input().split())))
ary.sort(reverse=True)

cnt_qube(length,width,height)
#print(dp)
#print(ary)


ans = 0
has_answer = True
for i in range(19,-1,-1):
    if dp[i] == 0:
        continue

    have_x = False
    for j in range(n):
        if ary[j][0] == i:
            x = j
            have_x = True
            break#dp의 인덱스인 i에는 2의 i승의 크기를 갖는 큐브가 그 숫자만큼 필요함.
                 #그래서 그만큼 가지고 있나 확인하기 위해 ary[j][0]-->[j][1]의 값 찾아야함.

    if i == 0:#크기가 1인 큐브들의 경우에는 예외처리를 해줘야함.
        if have_x == False:
            has_answer = False
            #불가능
            break
        #있는데 개수가 부족한 경우
        if dp[0]>ary[x][1]:
            has_answer=False#불가능
            break
        #개수를 다 채운 경우
        ans += dp[0]
#        print("경우1",end = ' ')
#        print(dp[0])
        ary[x][1] -= dp[0]
        continue


    if have_x == False:#해당 큐브 사이즈가 없다는 말. 더 작은 사이즈의 큐브로 채워 넣어야함.
        dp[i-1] += dp[i]*8
        continue
    if dp[i] - ary[x][1] > 0:#ary[x][0]이 2인걸 찾아서 그 값의 ary[x][1] 데려와야함.
    #남는 경우를 말함. 공간이 더 남아있음
        ans += ary[x][1]
#        print("경우2", end=' ')
#        print(dp[i],ary[x][1])
#        print(ary[x][1])
        dp[i-1] += (dp[i]-ary[x][1])*8
        ary[x][1] = 0  # 굳이 할필요는 없는데 그래도 확실하게
        dp[i] = 0
        continue
    #dp[i] 채워야 하는 블록이 꽉 차는 경우 갖고 있는 큐브가 더 많거나 딱 맞게 있는 경우
    ans += dp[i]
#    print("경우3", end=' ')
#    print(dp[i])

    ary[x][1] -= dp[i]
    dp[i]=0

if has_answer:
    print(ans)
else:
    print(-1)
#print(dp)
#print(ary)
