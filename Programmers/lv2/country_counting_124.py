#124나라의 
#2시간 걸림. 중간에 막힘
#그리디로 보임
#한개한개 나열해보니까 3진법에서 10 -> 04 20->14 이런식으로만 바꿔주면 된다는 걸 알게 됨.
#근데, 여러개가 한꺼번에 나온느 경우가 있음.
#예를들면 1010101010 이런거는 0이 나오는데, 그래서 반복적으로 10 형태가 안나올때까지 구현해줌.
# 추가적으로 1 2 4 말고 계산결과로 3이 나오기도 함. 당엲하게 40 같은거에서 6빼주면 34가 되니까.,
#그래서 마지막에 3을 2로 전부 바꿔주면 됨. 1 2 4 순서니까 4 다음으로 작은 값은 2
#다른사람들 풀이도 찾아보자

from collections import deque


def solution(n):
    answer = ''
    stack = deque()
    while n != 0:

        stack.append(n % 3)
        n //= 3
        #print(stack)
    while len(stack) != 0:
        x = stack.pop()
        answer += str(x)

        if x == 0:
            answer = str(int(answer) - 6)
            i=1
            while len(answer) >= i+1 and answer[-i-1] == '0':
                answer = str(int(answer) - 6*10**i)
                i += 1
    answer = answer.replace('3','2')

    return answer
