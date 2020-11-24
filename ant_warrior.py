#개미 전사 문제(dp예시)
#식량 창고 개수 n, 각 창고들에 저장된 식량의 개수. 
#붙어 있는 식량 창고 털 수 없을 때 얻을 수 있는 식량의 최대값은?

n = int(input())
storage = list(map(int,input().split()))
get_food = [0]*n

get_food[0] = storage[0]
get_food[1] = storage[1]

for i in range(2,n):
    if (get_food[i-2] + storage[i]) > get_food[i-1]:
        get_food[i] = get_food[i-2] + storage[i]
    else:
        get_food[i] = get_food[i-1]

print(get_food[n-1])
