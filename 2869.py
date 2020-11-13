#달팽이는 올라가고 싶다

a,b,v = map(int,input().split())

day = (v-a)//(a-b)#3

while True:
    if (v <= day*(a-b)+a):
        day += 1
        break
    else:
        day += 1
print(day)
