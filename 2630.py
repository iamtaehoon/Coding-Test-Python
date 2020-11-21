#dp문제 풀어봄. 이렇게 푸는게 맞나? 왜 이런 문제를 dp라고 하는지 모르겠음! 풀이 찾아보기

def cutting_paper(array,i,j,length):
    global blue_paper_cnt
    global white_paper_cnt

    if length == 1:
        if array[i][j] == 1:
            blue_paper_cnt += 1
        else:
            white_paper_cnt += 1
        return
    #종이가 4장 16장 이래
    blue_spot_cnt = 0
    for x in range(i,i+length):
        for y in range(j,j+length):
            blue_spot_cnt += array[x][y]
            
    if (blue_spot_cnt != 0) and (blue_spot_cnt != length*length):
        cut_length = int(length/2)
        cutting_paper(array,i,j,cut_length)
        cutting_paper(array,i+cut_length,j,cut_length)
        cutting_paper(array,i,j+cut_length,cut_length)
        cutting_paper(array,i+cut_length,j+cut_length,cut_length)
    elif blue_spot_cnt == 0:
        white_paper_cnt += 1
        return
    else:
        blue_paper_cnt += 1
        return

n = int(input())
array = []
global blue_paper_cnt
global white_paper_cnt

blue_paper_cnt = 0
white_paper_cnt = 0
blue_spot_cnt = 0
white_spot_cnt = 0

for i in range(n):
    array.append(list(map(int,input().split())))
    for j in range(n):
        blue_spot_cnt += array[i][j]
    white_spot_cnt = n*n - blue_spot_cnt
#나눌때마다 n크기 줄어드는거 구현해줘야함
cutting_paper(array,0,0,n)

print(white_paper_cnt)
print(blue_paper_cnt)
