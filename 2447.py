def square(x,original_i,original_j):
    if x == 1 or 0:
        ary[original_i][original_j] = '*'#ary[][]# *이 나오게 설계.
    else:
        for i in range(original_i,original_i + x, x//3):
            for j in range(original_j,original_j+x, x//3):
                if not ((i == original_i + x//3) and (j == original_j + x//3)):
                    square(x//3,i,j)
                else:
                    pass

n = int(input())
ary = [[' ']*n for _ in range(n)]

square(n,0,0)
for i in range(n):
    for j in range(n):
        print(ary[i][j],end = '')
    print()
