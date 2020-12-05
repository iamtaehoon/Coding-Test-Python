#브루트포스 문제
#3자리 야구문제인데 예외처리하기 너무 짜증났음..
#이런 브루트 포스 문제를 풀 때는 먼저 알고리즘을 종이에 다 쓰고 풀기
#코드가 굉장히 난잡한가,..?
#1. 먼저 말한 숫자들을 전부 리스트에 넣어서 저장,.
#2. 123부터 하나하나 999까지 예외는 빼놓고 다 테스트
#3. 테스트는 어케하냐. 비교해보고 스트라이크, 볼 개수 맞으면 아마 가능할거 카운트 1개 추가
#4. 이 카운트가 입력값 개수랑 똑같으면, 즉 말한 내용이 전부 일치하면 가능한 경우로 생각하고 카운트 한개 

import sys
input = sys.stdin.readline
n = int(input())
guess_result = []
for _ in range(n):
    guess_num, strike, ball = map(int,input().split())
    guess_num = str(guess_num)
    guess_result.append([guess_num,strike,ball])#튜플로 해도 되랴나

x= 123
result = 0
for x in range(123,1000):
    this_num_possible = True
    maybe_cnt = 0
    if x%10== 0:
        continue
    if (0 < x%100) and (x%100 < 10):
        continue
    x = str(x)
    if (x[0] == x[1]) or (x[0] == x[2]) or (x[1] == x[2]):
        continue
    #숫자가 같은 게 있으면 안됨
    for guess_num,strike,ball in guess_result:
        strike_cnt, ball_cnt = 0, 0

        if x[0] == guess_num[0]:
            strike_cnt += 1
        else:
            if x[0] == guess_num[1] or x[0] == guess_num[2]:
                ball_cnt += 1
        if x[1] == guess_num[1]:
            strike_cnt += 1
        else:
            if x[1] == guess_num[0] or x[1] == guess_num[2]:
                ball_cnt += 1
        if x[2] == guess_num[2]:
            strike_cnt += 1
        else:
            if x[2] == guess_num[0] or x[2] == guess_num[1]:
                ball_cnt += 1
        #print(guess_num,x,strike,strike_cnt,ball,ball_cnt)
        if strike_cnt != strike or ball_cnt != ball:
            this_num_possible = False
            break
        maybe_cnt +=1

    if maybe_cnt == n:
        #print(x)
        result += 1
#print("답은 ",end = ' ')
print(result)


