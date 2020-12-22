#덱을 구현하는 쉬운 문제임.
#input 하면 시간초과임
#split()했을때 뭐 없으면 그냥 안쪼개줌. 즉, 경우의수를 나눌 필요가 없었다는 뜻


from collections import deque
import sys


queue = deque()
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
	#print(queue)
	order = sys.stdin.readline().rstrip()
	if order == 'front':
		try:
			print(queue[0])
		except:
			print(-1)
		continue
	if order == 'back':
		try:
			print(queue[-1])
		except:
			print(-1)		
		continue
	if order == 'size':
		print(len(queue))
		continue
	
	if order == 'empty':
		if len(queue) == 0:
			print(1)
		else:
			print(0)
		continue
	if order == 'pop_front':
		try:
			print(queue.popleft())
		except:
			print(-1)
		continue
	if order == 'pop_back':
		try:
			print(queue.pop())
		except:
			print(-1)		
		continue
	
	order, x = order.split()
	
	if order == 'push_front':
		queue.appendleft(x)
		continue
	if order == 'push_back':
		queue.append(x)
		continue
