import sys

t = int(input())
for _ in range(t):  # 테스트 케이스의 개수
    n = int(input())
    lst = sorted([list(map(int, sys.stdin.readline().strip().split())) for x in range(n)], #입력이 많을때 사용하는거 이걸 쓰면 입력이 훨씬 빨라짐
                 key=lambda x: x[0])

    num = 1  # 1명은 무조건있지. 1등 1등일때
    min = lst[0][1]

    for i in range(1, n):
        if lst[i][1] < min:
            min = lst[i][1]
            num += 1

    print(num)