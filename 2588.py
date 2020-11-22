#시간초과가 나서 엥? 분할로 해서 풀었는데도 시간초과가 나면 어떡하나 싶어서 
# 코드의 효율을 높여보려다가 pypy로 했더니
# 그냥 문제가 풀렷음...

import sys

def cutting_paper(array, i, j, length):
    global paper_1_cnt
    global paper_0_cnt
    global paper_minus1_cnt
    if length == 1:
        if array[i][j] == 1:
            paper_1_cnt += 1
        elif array[i][j] == -1:
            paper_minus1_cnt += 1
        else:
            paper_0_cnt += 1
        return

    # 종이가 4장 16장 이래
    spot_minus1_cnt = 0
    spot_1_cnt = 0
    for x in range(i, i + length):
        for y in range(j, j + length):
            if array[x][y] == -1:
                spot_minus1_cnt -= array[x][y]
            else:
                spot_1_cnt += array[x][y]
    spot_0_cnt = length * length - spot_1_cnt - spot_minus1_cnt
    #print(spot_0_cnt,spot_1_cnt,spot_minus1_cnt)
    if (spot_0_cnt != length*length) and (spot_1_cnt != length * length) and (spot_minus1_cnt != length*length):
        cut_length = int(length / 3)

        for row in range(i,i+3*cut_length,cut_length):
            for col in range(j,j+3*cut_length,cut_length):
                cutting_paper(array, row, col, cut_length)

    elif (spot_0_cnt == length*length):
        paper_0_cnt += 1
        return
    elif (spot_1_cnt == length*length):
        paper_1_cnt += 1
        return
    else:
        paper_minus1_cnt +=1
        return


n = int(input())
array = []
global paper_1_cnt
global paper_0_cnt
global paper_minus1_cnt

paper_1_cnt = 0
paper_0_cnt = 0
paper_minus1_cnt = 0

spot_minus1_cnt = 0
spot_1_cnt = 0
spot_0_cnt = 0

for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
#    for j in range(n):
#        if array[i][j] == -1:
#            spot_minus1_cnt -= array[i][j]
#        else:
#            spot_1_cnt += array[i][j]
#    spot_0_cnt = n * n - spot_1_cnt - spot_minus1_cnt

# 나눌때마다 n크기 줄어드는거 구현해줘야함
cutting_paper(array, 0, 0, n)

print(paper_minus1_cnt)
print(paper_0_cnt)
print(paper_1_cnt)
