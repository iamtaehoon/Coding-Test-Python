#설탕 배달
#N을 입력받음. N킬로그램을 배달해야 하는데, 3키로 5키로 짜리가 있음. 최소로 들고갈 수 있는 봉지는 몇 봉지인가? 만약 불가능하면 -1을 출
def deliverMin(N, x):
    if x < 0:
        print(-1)
    else:
        namuji = N - 5 * (x) #18 - 3*5 안되면 18 - 2*5

        if (namuji % 3) == 0:
            print(int(namuji/3) + x)
        else:
            deliverMin(N,x-1)
N = int(input())



x = N//5 #18, 19 같은경우 3

deliverMin(N, x) #18이면 3, 21이면 4 이런거 넣어줌