#시간복잡도가 n^2이 나와 시간 초과가 나옴.
#로그복잡도로 만들어줘야할거같음. 아무래도 분할해서 풀어야 할 것 같은데
#막혀서 다음번에 풀어봐야겠다.
#1차 시도: 20/11/29
import sys
input = sys.stdin.readline

x = list(map(int, input().split()))
while x[0] != 0:

    max_rect = int(-1e9)
    for i in range(1,x[0]+1):
        length = 1
        height = x[i]
        j = i - 1
        k = i + 1
        while (j>=1):
            if x[j] < height:
                break
            j -= 1
            length += 1
        while(k<=len(x)-1):
            if x[k] < height:
                break
            k += 1
            length += 1
        #print(length,end=' ')
        #print(length*height)
        if max_rect < length*height:
            max_rect = length*height
    print(max_rect)

    x = list(map(int, input().split()))
