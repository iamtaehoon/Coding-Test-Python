#1011 Fly me to the Alpha Centauri

t = int(input())

for _ in range(t):
    x,y = map(int,input().split())
    distance = y-x
    if distance != 1:
        a= int((distance-1)**0.5)

        if(distance)<=a*(a+1):
            print(2*a)
        else:
            print(2*a+1)
    else:
        print(1)
