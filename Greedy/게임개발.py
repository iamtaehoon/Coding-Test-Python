n,m = map(int,input().split())
a,b,see = map(int,input().split())
ary = []#만들어야댐

for _ in range(n):
    ary.append(list(map(int,input().split())))
#print(ary)

nx = [0,-1,0,1]
ny = [-1,0,1,0]
visit_cnt = 1
try_cnt = 0

while(try_cnt < 4):
    check_x = a + nx[see]
    check_y = b + ny[see]
    see = (4+see-1)%4

    if ary[check_x][check_y] == 1:
        try_cnt += 1
        continue
    ary[check_x][check_y] = 1
    a = check_x
    b = check_y
    visit_cnt += 1
    try_cnt = 0

print(visit_cnt)
