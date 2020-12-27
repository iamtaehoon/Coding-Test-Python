#다리를 지나는 트럭.
#시간을 하나하나 추가해주면서
#배열로 다리를 만들어놓고 거기에 트럭의 무게를 하나씩 추가해주기
#맨처음에 이 방법으로 안풀고 다른 방법으로 풀었음. 시간복잡도가 안전하다는 생각이 들지 않았기때문
#그래서 시간복잡도를 어떻게 구할수있는지 이 문제에서, 그걸 찾아보기

#그래서 복잡하게 혼자 다리를 건너는 경우, 두개가 붙어, 3개가 붙어 건너는 형태로 구현했는데
#다리에서 트럭이 나가는 경우에서 계산이 너무 복잡해짐. 구현 못하고 인터넷 찾아봤는데 나같은 풀이가 없었음.

from collections import deque
def solution(bridge_length, weight, truck_weights):

    answer = 0#time
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    passing_weight = 0

    while truck_weights:
        answer += 1

        bridge_out = bridge.popleft()
        passing_weight -= bridge_out

        if passing_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            new_weight = truck_weights.popleft()
            bridge.append(new_weight)
            passing_weight += new_weight
    while passing_weight > 0:
        answer += 1
        bridge_out = bridge.popleft()
        passing_weight -= bridge_out

    return answer
