#누수를 막기위해 몇개의 스티커를 붙일거야? 문제
# 정렬해서 가장 왼쪽에 있는 누수부터 스티커를 붙여보기
# 스티커를 붙이는 상황은 3가지. 이미 붙어있어서 안붙여도 됨, 시작점은 붙어있는데 끝점이 안붙어서 스티커 이어붙이기, 시작점도 안붙어있어서 그냥 아예ㅒ 붙여버리기

cnt_leaks, len_tape = map(int,input().split())
ary = list(map(int,input().split()))
ary.sort()
range_ary =[]

for i in range(cnt_leaks):
	range_ary.append([ary[i]-0.5,ary[i]+0.5])
#print(range_ary)

i=0
cnt_tape = 0
#붙이고 끝점 표시
#첫번째거 여기서 해야함 예외처리때문에
end_tape = range_ary[0][0]+len_tape
cnt_tape += 1

while i<len(ary)-1:#1개일 때 예외처리해줘야함
	i += 1
	if range_ary[i][1]<=end_tape:#다음 구멍의 테이프 끝 부분이 현재 붙인 테이프 안에 있을 경우
		continue
	elif range_ary[i][0] > end_tape:#테이프 시작 부분이 현재 테이프보다 밖에 있을 경우
		cnt_tape += 1
		end_tape = range_ary[i][0] + len_tape
	elif range_ary[i][1]>end_tape:#else, 테이프 시작 부분이 겹치기는 한데, 끝나는 점이 밖에 있을 경우
		cnt_tape += 1
		end_tape += len_tape
	
	#물새는곳 한개한개 틀어막아야지 한개씩 데리고와
	#sticker 붙여
	#그 스티커 끝 범위 표시해줘
	#위로 올라가서 다음 물새는곳 찾아줘
	
print(cnt_tape)
