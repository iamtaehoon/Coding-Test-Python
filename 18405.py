#역시 문제를 똑바로 보지 않음 n*n 정방형인데 n*m으로 잘못보고 한참을 끙끙댐. 문제를 제대로 읽는 습관을 들여야함. 계속 같은 실수 반복
#먼저 문제를 봤을때, 바이러스들이 다 다르게 있는데 어떻게 우선순위를 구하지라는 생각을 했다.
# 생각하다보니 아예 거꾸로 생각을 해서 입력값에서부터 bfs를 해줘 가장 가까운 바이러스를 찾으려 했다.
#더 깊게 생각했어야 하는데, 그러지 못하고 문제를 풀었음.
#결과적으로 반례가 존재한다. 
# 0 0 0 0 0 0 4
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 2 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 3 0 0 0 0 0 T

#3이 가장 가깝지만 2가 막아버려서 결과적으로 가장 가까운건 4가 됨.
#짧게 생각한 이유. 신박한 아이디어라고 생각해서 순간 흥분함...

#다른 사람들의 풀이를 보고 다시 풀어보자.
