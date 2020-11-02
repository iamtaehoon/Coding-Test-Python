#시뮬레이션 너무 어려워... 짜증나 실수 어떻게 줄이지?
#1. 생각 부족: 꼬릴 어떻게 처리할지 몰랐음. 계속 담아주고 pop하는 식으로
# 2. 사과를 먹으면 없어지는데 그 처리를 하지 않음. 이런 사소한 실수들 고쳐나가는 연습. 손을 최대한 다 코딩해두고 코딩하기
#그러기 위해서 잘하는 사람들의 손코딩 참고하기

n = int(input())#보드의크기 n
k = int(input())#number of apple

time_turn = []
ary = [[0]*n for _ in range(n)]
d = [[0]*n for _ in range(n)]


#테일에서 2번째 거 정보 저장해주는 게 필요할거 같은데? 그래야 몸 틇었을때 어디로 틀지를 가르쳐주지
head_x, head_y = 0,0
d[head_x][head_y] = 1
tail=[]
tail.append([head_x, head_y])
#print(ary)

for _ in range(k):
    apple_x,apple_y = list(map(int,input().split())) #사과의 위치
    ary[apple_x-1][apple_y-1] = 2 # 사과를 2로 표현


l = int(input()) # 방향 변환 횟수
for _ in range(l):
    time_turn.append(list(input().split())) #초, L or D 입력 # 아니면 3 4로 왼쪽으로 틀지 오른쪽으로 틀지가르쳐주면안댐?

see = 0
def turn_snake(x):
    global see
    if x == 'L':
        see += 1
        #왼쪽으로 고개돌림
    else:#오른쪽으로 고개돌림
        see -= 1

    if see == -1:
        see = 3
    elif see == 4:
        see = 0


dx = [0,-1,0,1]#동북서남
dy = [1,0,-1,0] #왼쪽으로 고개를 돌리면, ---> 오른쪽고개돌리면: <---

cnt = 0
turn_cnt = 0
while True:#뱀 움직 시작 #몇번이나 while문 도는지 확인해서 그게 바로 카운트임

    for i in range(len(time_turn)):
        if cnt == int(time_turn[i][0]):
            turn_snake(time_turn[i][1])
    cnt += 1

    head_x = head_x + dx[see]
    head_y = head_y + dy[see] #머리 내밀어봄
    tail.append([head_x,head_y])

    if 0 > head_x or 0> head_y or n <= head_x or n<=head_y or d[head_x][head_y] == 1: # 벽에 부딫히거나 몸에 부딫히면
        break

    elif ary[head_x][head_y] == 2:
        d[head_x][head_y] = 1
        ary[head_x][head_y] = 0

    else: #사과 못먹음
        d[head_x][head_y] = 1

        d[tail[0][0]][tail[0][1]] = 0
        tail.pop(0)

print(cnt)
