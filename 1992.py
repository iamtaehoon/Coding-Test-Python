#순서에 유의하면서 풀기! 결과값이 순서값에 따라 다르게 

def quad_tree(array,i,j,length):

    if length == 1:
        if array[i][j] == 1:
            print('1',end='')
        else:
            print('0',end='')
        return

    cnt_1 = 0
    for x in range(i,i+length):
        for y in range(j,j+length):
            cnt_1 += array[x][y]

    if (cnt_1 != 0) and (cnt_1 != length*length):
        cut_length = int(length/2)
        print('(',end='')
        quad_tree(array,i,j,cut_length)
        quad_tree(array,i,j+cut_length,cut_length)
        quad_tree(array,i+cut_length,j,cut_length)
        quad_tree(array,i+cut_length,j+cut_length,cut_length)
        print(')',end='')
    elif cnt_1 == 0:
        print('0',end='')
        return
    else:
        print('1',end='')
        return

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input())))
#나눌때마다 n크기 줄어드는거 구현해줘야함
quad_tree(array,0,0,n)
