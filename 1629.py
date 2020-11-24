#분할정복: 부분최적구조를 만족 시켜야함. ㅠㅠ

def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % C
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % C # b가 짝수인 경우
        else:
            return temp * temp * a % C # b가 홀수인 경우

A, B, C = map(int, input().split())

result = power(A, B)
print(result)


'''
#실패 코드. 분할 정복을 이런 느낌으로 푸는 줄 알았는데 완전 아니었음.
# 나머지는 어차피 반복될거라고 생각했는데, 안그런 경우들도 있지 않음? 모든 경우에 맞는 그런 알고리즘. 점화식을 짜야함

a, b, c = map(int,input().split())
num = a
list_namuji = []
x = None
cnt = 0

while(True):#이번에 들어오는 값이 리스트_나머지에 없으면
    namuji = num % c
    num = namuji * a
    cnt += 1
    if namuji in list_namuji:
        break
    list_namuji.append(namuji)

#여기 있다는건 나머지로 나온 값이 기존에 리스트에 이미 존재하는 값이라는 것.
#cnt는 지금 나온 나머지의 인덱스, 기존에 리스트에 존재하던 인덱스 찾아줘야
start = list_namuji.index(namuji)

list_namuji = list_namuji[start:]
#반복
answer_index = (c-start-1)%len(list_namuji)
#print(list_namuji)
print(list_namuji[answer_index])
'''
