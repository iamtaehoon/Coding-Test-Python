#18423 감시 

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
