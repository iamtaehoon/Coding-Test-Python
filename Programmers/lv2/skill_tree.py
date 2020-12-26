#스킬트리 찍는 문제

#위상정렬로 풀까 하다가 스킬트리가 한 개만 있는거 확인하고 간단한 문제라고 생각함.

#맨 처음에는 skill_trees 한개씩 가져와서
#스킬트리에 없는 문자 전부 날리고 공백이 된 문자를 answer에 추가
#첫 문자 c로 시작 안하는 문자 전부 날림, c지워주고 공백이 된 문자열을 정답에 추가
#두번째 문자 b 반복..... 마지막 문자가 나올때까지. 마지막 문자가 되면 계산 안하고 살아있는 문자열들을 전부 정답에 추가
#이케 하려 했는데, 문자열 처리가 너무 힘들어서 비슷하지만 다른 방법으로 구현

# 각 문자들을 한 개 한 개 나오게 해서 만약 문자열이 나왔는데, 순서에 맞지 않은 문자열이 나오면 is_Correct를 false 처리해줌.


def solution(skill, skill_trees):
    answer = 0

    for each_skill_tree in skill_trees:#스킬트리에서 스킬묶음을 한개 가져옴.
        is_Correct = True
        i = 0

        for each_skill in range(len(each_skill_tree)):#그 스킬들을 한개한개 .
            if (each_skill_tree[each_skill]) in skill:#그 스킬이 스킬트리 안에 있는거면
                #print(each_skill_tree[each_skill])

                #문자가 나오면 그 문자는 첫 문자여야해
                #또 문자가 나오면 그 문자는 두번째 문자여야해
                #또 문자가 나오면 그건 세번째...
                #이렇게 이상 없이 나오면 초기화해주고 정답을 1 늘려준다.

                if each_skill_tree[each_skill] == skill[i]:
                    i += 1
                else:#each_skill_tree[each_skill] != skill[i]:
                    is_Correct = False
                    break#한개한개 가져오는걸 break
        if is_Correct == True:
            answer += 1

        #print()

    return answer

skill = "CBD"
skill_trees = ["BACDE","CBADF", 'AECB',"BDA"]
print(solution(skill,skill_trees))
