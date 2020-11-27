#40보다 작거나, 같은! 문제 조건 저게 왜 눈에 안들어왔지...
#dp문제. 메모이제이션을 사용해서 푸는데, 0이랑 1 개수도 피보나치를 따라감

t = int(input())
fibo = [[0,0] for _ in range(41)]
fibo[0] = [1,0]
fibo[1] = [0,1]

for i in range(2,41):
	first,second = fibo[i-2]
	third, fourth = fibo[i-1]
	
	fibo[i] = [first+third,second+fourth]

for _ in range(t):
	num = int(input())
	answer_0, answer_1 = fibo[num]	
	print(str(answer_0)+' '+str(answer_1))
