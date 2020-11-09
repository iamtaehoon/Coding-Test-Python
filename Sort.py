#선택 정렬
array_selection = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array_selection)):
    min_index = i
    for j in range(i+1, len(array_selection)):
        if array_selection[min_index] > array_selection[j]:
            min_index = j
    array_selection[i], array_selection[min_index] = array_selection[min_index], array_selection[i]

print(array_selection)


#삽입정렬
array_insection = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array_insection)):#첫번째거는 맞으니까!
    for j in range(i,0,-1):#j는 인덱스 i부터 1까지 1씩감소하는 인덱스
        if array_insection[j-1] > array_insection[j]:
            array_insection[j],array_insection[j-1] = array_insection[j-1], array_insection[j]
        else:#계속 데이터가 앞으로 가다가, 나보다 작은 데이터랑 비교하게 됐어. 그럼 거기서 중단하고, 다음 인덱스의 데이터를 비
            break
print(array_insection)


#퀵 정렬

array_quick = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array_quick, start, end):#start,end 에 인덱스 입력
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소, 인덱스 번호
    left = start + 1
    right = end
    while (left <= right):
        while(left<=end and array_quick[left] <= array_quick[pivot]):#left에서 시작한게 피벗보다 작은 값을 찾아야하는데, 못찾을수도있지?
            left += 1                                                #못찾으면 left를 적당히 키울수있을만큼만 키워야지 안그래?
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array_quick[right] >= array_quick[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array_quick[right], array_quick[pivot] = array_quick[pivot], array_quick[right]#right가 더 작아졌으니까 말이 right지
                                                                                            #사실 이게 left값이 된거임
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array_quick[left], array_quick[right] = array_quick[right], array_quick[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array_quick, start, right - 1)#right가 피벗이랑 바꼈으니까 right첫번째 값이 원래 pivot임!
    quick_sort(array_quick, right + 1, end)

quick_sort(array_quick, 0, len(array_quick) - 1)
print(array_quick)








#퀵정렬 in Python
array_quick2 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


print(quick_sort2(array_quick2))





