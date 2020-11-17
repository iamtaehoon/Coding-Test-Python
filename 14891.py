#풀기는 풀었는데, 코드가 난잡하다는 생각이 듬.
#정리할 엄두는 아직 안나고
#구현 , 시뮬레이션 이쪽 파트가 약하다고 느껴짐.
# 쉬운 문제들로 연습 좀 해보고 싶다

def move_gear(gear_num, moving_direction):
    if gear_status[gear_num-1][3] == False:
        gear_way[gear_num-1] = moving_direction
        if gear_num == 1:
            gear_status[0][3] = True
            if (gear_1[gear_status[0][1]] != gear_2[gear_status[1][0]]):#1's right 2's left 자성이 다르면
                move_gear(2,-moving_direction)
        elif gear_num == 2:
            gear_status[1][3] = True
            if (gear_2[gear_status[1][1]] != gear_3[gear_status[2][0]]):
                move_gear(3,-moving_direction)
            if (gear_2[gear_status[1][0]] != gear_1[gear_status[0][1]]):
                move_gear(1,-moving_direction)
        elif gear_num == 3:
            gear_status[2][3] = True
            if (gear_3[gear_status[2][1]] != gear_4[gear_status[3][0]]):
                move_gear(4,-moving_direction)
            if (gear_3[gear_status[2][0]] != gear_2[gear_status[1][1]]):
                move_gear(2,-moving_direction)
        elif gear_num == 4:
            gear_status[3][3] = True
            if (gear_4[gear_status[3][0]] != gear_3[gear_status[2][1]]):
                move_gear(3,-moving_direction)



    #여러개 글로벌 처리해주는 게 있나?



gear_1 = list(map(int,input()))
gear_2 = list(map(int,input()))
gear_3 = list(map(int,input()))
gear_4 = list(map(int,input()))
gears = [gear_1,gear_2,gear_3,gear_4]
gear_status= [[6,2,0,False],[6,2,0,False],[6,2,0,False],[6,2,0,False]]
gear_way = [0,0,0,0]
#gear_1_left_index, gear_1_right_index, gear_1_up_index,is_gear_1_move
#gear_2_left_index, gear_2_right_index, gear_2_up_index,is_gear_2_move = 6,2,0,False
#gear_3_left_index, gear_3_right_index, gear_3_up_index,is_gear_3_move = 6,2,0,False
#gear_4_left_index, gear_4_right_index, gear_4_up_index,is_gear_4_move = 6,2,0,False

k = int(input())
for _ in range(k):
    gear_num, moving_direction = map(int,input().split())
    move_gear(gear_num,moving_direction)

    #print(gear_status)
    for i in range(4):
        if (gear_status[i][3] == True):
            gear_status[i][0] = (gear_status[i][0]+8-gear_way[i])%8
            gear_status[i][1] = (gear_status[i][1]+8-gear_way[i])%8
            gear_status[i][2] = (gear_status[i][2]+8-gear_way[i])%8
            gear_status[i][3] = False

    #print(gear_status)
    #print(gear_way)

    gear_way[0] = 0
    gear_way[1] = 0
    gear_way[2] = 0
    gear_way[3] = 0


result = 0
for i in range(4):
    if gears[i][gear_status[i][2]] == 1:

        result += 2**i
print(result)
