n,m,x,y,k = map(int,input().split())
ary = []
for _ in range(n):
    ary.append(list(map(int,input().split())))
move_order= list(map(int,input().split()))

#범위는 0<= <n, 0<= <m
#ip,down,left,right = 북, 남, 서, 동
dice_now,dice_bottom, dice_up, dice_down, dice_left, dice_right= 1, 6, 5, 2, 3, 4#위로 굴릴때 아래로 굴릴때 왼 오 굴릴때 즉. 이동방향, up을 하면 이동하는 곳, left를 하면 이동하는 곳

dice_stored_num = [0]*6 #초기값
#1,2,3,4:  동서북남
dx = [0,0,-1,1]
dy = [1,-1,0,0]


for move_direction in move_order: # 1 2 3 4 동 서 남 북 입
    #ary[0]

    nx = x + dx[move_direction-1] # 1,2,3,4 --> 0,1,2,3
    ny = y + dy[move_direction-1]

    if nx < 0 or ny < 0 or nx >= n or ny >= m:#범위 벗어남 그럼 그냥 무시
        continue
    else:#움직였으니까 1. 좌표 최신화. 2. dice_now 포함 다 세팅 3. 각 123456이 담고있는 0에 값 담기 아직 구현 x 리스트[0,0,0,0,0,]
        x = nx
        y = ny
#now, up, left가 중요함
        if move_direction == 1:#오른쪽으로 움직이겠다
            dice_left = dice_now #now가 밑에서 바뀌니까 left부터 변경
            dice_now = dice_right
        elif move_direction == 2:#왼쪽으로움직였다
            dice_now = dice_left
            dice_left = dice_bottom
        elif move_direction ==3: # 북쪽으로 움직
            dice_now = dice_up
            dice_up = dice_bottom
        elif move_direction ==4: #남쪽, 아래로 움직였다
            dice_up = dice_now
            dice_now = dice_down

        #핵심 아이디어 왼오 움직일때는 위아래 안바뀌고 위아래 움직일땐 왼오 안바뀌;ㅁ
        dice_bottom = 7 - dice_now
        dice_down = 7 - dice_up  # 2
        dice_right = 7 - dice_left  # 4

    if ary[x][y] == 0:
        ary[x][y] = dice_stored_num[dice_bottom-1]
    else:
        dice_stored_num[dice_bottom-1] = ary[x][y]#바닥면에 지도에 쓰여진숫자 복사
        ary[x][y] = 0

    print(dice_stored_num[dice_now - 1])

    #print(dice_now,dice_bottom, dice_up, dice_down, dice_left, dice_right) #이제 이 값들은 그저 인덱스일뿐. 1 2 3 4 5 6 이라는 자리에 숫자를 넣어줄거임.
