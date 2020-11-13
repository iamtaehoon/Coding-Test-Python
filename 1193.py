import sys
n= int(sys.stdin.readline())
i=1
diag_len = 0
cnt = 0
x = n
top_bottom = False
while True:
    diag_len += 1
    n = n - diag_len
    if n<=0:
        break
    else:
        if top_bottom == True:
            top_bottom = False
        else:
            top_bottom = True

        cnt += diag_len


a = str(x-cnt)
b = str(diag_len+1 - (x-cnt))
if top_bottom == True:
    print(a+'/'+b)
else:
    print(b+'/'+a)

#x - cnt#이만큼 이동해야함
