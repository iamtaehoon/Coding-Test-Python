def solution(InputArr):
    answer = 0
    endTime = 0
    for i in range(len(InputArr)):  # 끝시간을 기준으로 정렬을 함
        if endTime <= InputArr[i][0]:  # 시작시간
            endTime = InputArr[i][1]  # 끝시간 #가장 빨리 끝나는 회의의 끝시간이 endtime으로 들어감. 그 다음에 시작할 수 있는거
            answer += 1
    return answer


N = int(input())
InputArr = []

for i in range(N):
    A, B = map(int, input().split())
    InputArr.append([A, B])

InputArr.sort(key=lambda x: (x[1], x[0]))
print(solution(InputArr))