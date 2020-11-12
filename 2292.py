import sys

n = int(sys.stdin.readline())
n = n-1
cnt = 1
wave = 1
while True:
    if n<=0:
        break
    else:
        n -= 6*wave
        wave+=1
        cnt+=1
print(cnt)
