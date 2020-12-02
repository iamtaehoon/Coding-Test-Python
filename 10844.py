#쉬운 계단수
#점화식 못찾아서 답지 찾아봄.
#아 ex)3으로 시작하는 3자리수는 2로시작 2자리수 + 4로시작 2자리수구나.
#근데 코딩이 계속 안되서 그냥 답보고 함
#0일때를 생각해줘야 하는구나. 0일 때도 계속해서 경우의수들 더해줘야함

stair_numbers = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 101):
    for j in range(10):
        if i == 1:
            stair_numbers[i][j] = 1
        else:
            if 1 <= j <= 8:
                stair_numbers[i][j] = stair_numbers[i - 1][j - 1] + stair_numbers[i - 1][j + 1]
            elif j == 0:
                stair_numbers[i][j] = stair_numbers[i - 1][j + 1]
            elif j == 9:
                stair_numbers[i][j] = stair_numbers[i - 1][j - 1]

N = int(input())
print(sum(stair_numbers[N][1:10]) % 1000000000)
