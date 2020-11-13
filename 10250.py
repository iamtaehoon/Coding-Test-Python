#acm호텔

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    floor = n%h
    if floor == 0:
        floor = h

    num = (n-1)//h +1

    print('{0}{1:02d}'.format(floor,num))
