#18428 감시 

#아이디어. 직선을 그어놓고. 직선의 개수-교점의 개수로 풀었다.
#이 개수가 3개보다 작거나 같으면 장애물 3개로 시야를 다 가릴 수 있음.
#다만, 생각을 하지 못했던 부분이, ST가 붙어있는 경우를 생각하지 못해서 좀 오래걸림

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
array = []
teacher_list = []
cnt_1 = 0
cnt_2 = 0

for _ in range(n):
    array.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if array[i][j] == 'T':
            teacher_list.append((i,j))
teacher_see = list()

for teacher in teacher_list:
    original_x,original_y = teacher
    for i in range(4):
        x, y = teacher
        while True:
            nx = x +dx[i]
            ny = y +dy[i]
            if nx<0 or ny<0 or n<=nx or n<=ny:
                break
            if array[nx][ny] == 'T':
                break
            x = nx
            y = ny
            if array[x][y] == 'S':
                #사이에 잇는 값들 전부 teacher_see에 저장
                cnt_1 +=1
                if (x-dx[i] == original_x and y-dy[i] == original_y):
                    cnt_1 = 1e9
                while not (x-dx[i] == original_x and y-dy[i] == original_y):
                    x= x - dx[i]
                    y= y - dy[i]
                    teacher_see.append((x,y))
                break
#print(teacher_list) #선생님이 있는 좌표들을 모아둔 리스트
#print(teacher_see) #선생과 학생 사이에 있는 빈 공간들의 좌표
#print(cnt_1) #1번 카운트

teacher_see = list(set(teacher_see))
#print(teacher_see)
for between_location in teacher_see:#between location is 둘 사이의 거리 한개한개
    cnt_meet = 0
    original_x,original_y = between_location
    for i in range(4):
        x, y = between_location
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or n<=nx or n<=ny:
                break
            x = nx
            y = ny
            if array[x][y] == 'T' or array[x][y] == 'S':
                cnt_meet += 1
                break
    if cnt_meet == 4:
        #print("교점이 생기는 부분")
        #print(original_x,original_y)
        cnt_2 += 1
    if (cnt_1 - cnt_2) <=3:
        print('YES')
        break
if (cnt_1- cnt_2) > 3:
    print("NO")
#print(cnt_1)
#print(cnt_2)



''' #전체탐색을 사용하는 풀이 2
from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도 정보 (N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

#특정 방향으로 감시를 진행
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():#학생이 감지되면 true 아니면 false
    # 모든 선생의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False#한명도 학생이 감지되지 않도록 설치할 수 있는가 여부

#빈 공간에서 3개를 뽑는 모든 조합
for data in combinations(spaces,3):#2개씩 묶음 되있는 친구를 3개 뽑는거!
    for x,y in data:
        board[x][y] = 'O'

    if not process():
        find = True
        break
    for x,y in data:
        board[x][y] ='X'

if find:
    print('YES')
else:
    print('NO')








'''
