#https://programmers.co.kr/learn/courses/30/lessons/42587
#생각은 제대로 했는데, 구현에서 실수를 좀 함.


from collections import deque
answer = 1
def solution(priorities, location):
    global answer
    queue = deque(priorities)

    while True:

        now_priority = queue[0]
        cnt = 0
        for i in range(1,len(queue)):
            next_priority = queue[i]
            cnt += 1
            if next_priority > now_priority:
                queue.append(queue.popleft())
                location = (len(queue) + location - 1) % len(queue)
                #print(queue, location, answer)
                #print(queue)
                break
        if cnt == len(queue)-1:
            break
        #for문을 다 돌림. 그 말은 지금 값이 가장 우선순위가 높아 복사해야 하는 수라는 뜻.

    if location != 0:
        queue.popleft()
        answer += 1
        location = (len(queue) + location - 1) % len(queue)
        #print(queue,location,answer)
        solution(queue,location)
    #location이 0이라는 말.

    return answer
