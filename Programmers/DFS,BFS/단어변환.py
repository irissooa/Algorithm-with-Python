'''
begin이 target으로 변환돼야되는데 한번에 한개의 알파벳만 바꿀수 있고 그 단어가 words에 있는 단어야 된다.
1. begin과 target이 다른 것을 words에 있는 단어 중 begin과 같은 단어가 1개 차이나고 target과 begin이랑 공통되는 것이 1개 더 많아야된다.
2. 바뀐 것으로는 다시 바뀌지 않게 words에서 뺴줌
'''


def solution(begin, target, words):
    answer = 0
    bigin_target_cnt = 0
    for i in range(len(begin)):
        if begin[i] == target[i]:
            bigin_target_cnt += 1
    print('begin과 target공통', bigin_target_cnt)
    while True:
        if begin == target:
            break
        change_target = [0, 0]
        for i in range(len(words)):
            word = words[i]
            begin_cnt = 0
            target_cnt = 0
            for w in range(len(word)):
                if word[w] == begin[w]:
                    begin_cnt += 1
                if word[w] == target[w]:
                    target_cnt += 1
            if (begin_cnt == len(begin) - 1) and (change_target[1] < target_cnt):
                change_target = [i, target_cnt]
        if change_target != [0, 0]:
            print(begin, '->', words[change_target[0]])
            begin = words[change_target[0]]
            words.pop(change_target[0])
            bigin_target_cnt += 1
            answer += 1
        else:
            answer = 0
            break

    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))