#캠핑문제. 스케쥴을 그림 그려보니까 답이 바로 나와서 구현해줌. 이게 그리디인지는 모르겠음.

num = 0
while True:
	num += 1
	available, duration, total = map(int,input().split())
	if available == 0 and duration == 0 and total == 0:
		break
	y = 0
	x = total//duration
	total -= x*duration
	y += x*available

	if total > available:
		y += available
	else:
		y += total
	print("Case {0}: {1}".format(num,y))
