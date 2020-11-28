#인터넷에서 코드 따옴. 
#나는 원래 배열을 곱한 값들을 저장하는 리스트를 만드려고 했음.
#예를 들어 16제곱이면 8제곱값이 저장되어 있나? 안되어있으면 4제곱*4제곱을 재귀해서 찾아라
#4제곱이 있냐? 없으면 2제곱을 ... 이런 함수를 작성했는데, 내 코드에서는 무리없이 돌ㄷ아가지만 계속 런타임 에러가 뜸
#그래서 인터넷 보고 코드를 가져옴. 

#16이면 함수(16) --> 함수(8)*함수(8) --> 이런식으로 반복. 계속 반복되는 계산을 하는거같긴한데 이렇게 해서 오히려 풀림.
#아, 16은 8을 찾아와라 --> 4찾아와라-->2찾아와라.... 이런식으로 계산 반복이 안되는구나?

def make_matrix(A, matrix):
    # [[0]*2]*2 로 하면 리스트가 공유되서 다른 결과가 나옴
    dummy_matrix = [[0 for _ in range(N)] for _ in range(N)]
    
    # 행렬곱에서 사용한 방법은 시간 초과
    for i in range(N):
        for j in range(N):
            for k in range(N):
                dummy_matrix[i][j] += (matrix[i][k] * A[k][j])
            dummy_matrix[i][j] %= 1000

    return dummy_matrix

def matmul(A, B):
    if(B == 1):
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
       
        return A
    
    # 홀수인 경우엔, A를 마지막에 곱해주어야 합니다.
    # ex) AAAAA -> (A^2)^2 * A
    elif((B%2) == 1):
        matrix = matmul(A, B-1)
        new_matrix = make_matrix(A, matrix)
    
        return new_matrix
    
    # 짝수인 경우엔, 제곱수로 계속해서 곱해집니다.
    # ex) AAAA -> (A^2) = AA -> (A^2)^2 = AAAA
    else:
        matrix = matmul(A, B//2)
        new_matrix = make_matrix(matrix, matrix)
    
        return new_matrix

N, B = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

result = matmul(A, B)

for row in result:
    print(*row)
