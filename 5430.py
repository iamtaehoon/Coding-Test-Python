#5430
#맨 처음에 덱으로 풀려 했는데 시간초과.
#어떻게하지.. 하면서 답 보니까 시간복잡도때문이고 굳이 덱 안쓰고 인덱스 이용해서 풀 수 있을 거 같다는 생각을 함.
#근데 그렇게 풀었는데 틀림.. 아, [] 이 경우가 너무 헷갈린다. 이거 해결함.
#그래도 답 안나와서 왜일까 고민 계속했는데 [2, 1] 과 [2,1] 의 차이었음. ' ' 을 ''으로 바꿔주니 정답이 나옴 너무 짜증남 ㅠㅠ

T = int(input())

for _ in range(T):

    _reverse = False
    has_error = False

    order = input()  # ex.RDD
    num_ary = int(input())  # ex.4
    ary = input()  # ex.[1,2,3,4]
    ary = ary.replace('[', '').replace(']', '')
    ary = list(ary.split(','))
    # print(ary)
    start = 0
    end = num_ary - 1

    for i in range(len(order)):  # 0일때는 따로 처리할까
        if order[i] == 'R':
            if _reverse == True:
                _reverse = False
            else:
                _reverse = True
            continue
        # order[i] is 'D'
        if num_ary == 0:
            has_error = True
            break
        if _reverse == True:
            end -= 1
        else:
            start += 1
    #print(start,end)
    #print(ary)
    if has_error == True:
        print('error')
        continue
    if num_ary == 0:
        print('[]')
        continue
    if start == end + 1:
        print('[]')
        continue
    if start > end:
        print('error')
        continue  # error

    if _reverse == False:
        print(str(list(map(int,ary[start:end + 1]))).replace(' ',''))
    # end부터 start까지
    elif _reverse == True:
        if start == 0:
            print(str(list(map(int,ary[end::-1]))).replace(' ',''))
        else:
            print(str(list(map(int,ary[end:start-1:-1]))).replace(' ',''))
