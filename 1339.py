wordNum = int(input())
word = []
for i in range(int(wordNum)):
    word.append(list(input()))#ary 는 알파벳들 한개한개 담는 배열
print(word)
number = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

charDic = dict()
for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j] not in charDic:
            charDic[word[i][j]] = 10**(len(word[i])-j-1)
        else:
            charDic[word[i][j]] += 10 ** (len(word[i])-j-1)

keyList = list(charDic.keys()) # 알파벳들을 리스트로 만듬 abcdef
for i in range(len(keyList)-1):
    for j in range(len(keyList)-i-1):
        if charDic[keyList[j]] < charDic[keyList[j+1]]:
            keyList[j], keyList[j+1] = keyList[j+1], keyList[j]
#알파벳을 버블 정렬했음. 큰거 순서대로

result = 0
for i in keyList: # 큰거 순서대로 정렬되어서 i로 들어감. 그게 key가 되어서 charDic에서 그 알파벳의 개수를 찾음
    result += number.pop(0) * charDic[i]

print(result)
