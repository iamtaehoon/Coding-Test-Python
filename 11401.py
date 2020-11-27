#어떻게 풀어도 메모리 초과가 나길래
#하아.. 어떡하냐 해서 봤는데 페르마의 소정리라는걸 사용해야 했음!
#이거 말고도 4대 정리가 있다는데 그거 정도는 익혀둘까?
#페르마의 소정리 확실하게 이해가 가지는 않음 그렇지만 이 a^(p-1) 은 1과 합동
#a^-1은 a%p * (a^-1)%p = 1인거처럼, a%p * a^(p-1)%p =1, 그래서 a^(p-2)로 바꿔 쓸 수 있음. 나머지를 보는 부분에서는!!!

p = 1000000007
n,k = map(int,input().split())

def power(a,b):
	if b == 0:
		return 1
	if b%2:
		return (power(a,b//2)**2*a)%p
	else:
		return (power(a,b//2)**2)%p
	
fact = [1 for _ in range(n+1)]
for i in range(2,n+1):
	fact[i] = fact[i-1]*i%p
	
a = fact[n]
b = (fact[n-k]*fact[k]) %p

# (A/B) % p 
# = A * B^-1 % p 
# = A * B^-1 * B^p-1 % p 
# = A * B^p-2 % p 
# = (A % p) * (B^p-2 % p) % p 
print((A % p) * (power(B, p-2) % p) % p )
