#2775 부녀회장이 될테야

t = int(input())

for _ in range(t):
    k = int(input())#층, 호 순서대로 입력
    n = int(input())

    apart_resi = [[0 for col in range(n)] for row in range(k+1)]#n호 k층

    for j in range(n):
        apart_resi[0][j] = (j+1)

    for i in range(1,k+1):
        for j in range(n):#배열이 0부터 해서 n-1까지 있는데, 이건 1호부터 n호까지라는 듯임
            if j == 0:
                apart_resi[i][0] = 1
            else:
                apart_resi[i][j] = apart_resi[i-1][j] + apart_resi[i][j-1]#지금 1층 2호부터 시작[1][1]

    print(apart_resi[k][n-1])
