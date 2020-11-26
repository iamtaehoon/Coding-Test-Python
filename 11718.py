#어떻게 이걸 에러 안나고 처리하지...
#그 에러가 났을때 쓰는 문자가 뭐였지? --> EOFError
#try & except 코테에서 이걸 쓸거라 생각을 못했음.

while True:
    try:
        print(input())
    except EOFError:
        break
