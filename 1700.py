#생각은 맞게 했는데, 구현을 하지 못함.
#너무 복잡하게 생각했음. 여러가지 예외상황을 두려 하니 어디에선가 에러가 나는거 같음. 어디서 틀렸는지 초반 코드에서는 알 수가 없음
# 상황을 만들어서 거기에 맞춰 생각하면 편할듯.. 그리고 try/except 사용법 알아보기

n, k = map(int, input().split())
s = list(map(int, input().split()))
m = [0 for i in range(n)]
cnt = 0
for i in range(k):
    isTrue = False
    for j in range(n):
        if m[j] == s[i] or m[j] == 0:
            isTrue = True
            m[j] = s[i]
            break
    if isTrue:
        continue
    else:
        a = 0
        for j in range(n):
            try:
                if a < s[i + 1:].index(m[j]):
                    a = s[i + 1:].index(m[j])
                    b = j
            except:
                a = -1
                b = j
                break
        m[b] = s[i]
        cnt += 1
print(cnt)
