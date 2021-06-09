'''
그룹단어는 연속해서 나오는 단어!
만약 떨어져서 나온다면 그룹단어가 아니다.
1. 단어 입력받기
2. 현재 알파벳을 담을 변수, 다른 알파벳이 나오면 나왔던 알파벳을 담을 리스트에 담기
3. 나왔던 알파벳 리스트에 있는 단어가 다음 단어라면 그룹단어가 아니므로 지나감
'''
T = int(input())
cnt = 0
for tc in range(1,T+1):
    words = list(input())
    alpha = words[0]
    temp = []
    for w in range(1,len(words)):
        if alpha != words[w]:
            if words[w] in temp:
                break
            temp.append(alpha)
            alpha = words[w]
    else:
        cnt += 1
print(cnt)

