'''
1. 변경되는 크로아티아 알파벳을 리스트에 담아둔다
2. 입력받은 문자열을 앞에서부터 보면서 목록에 없는 글자는 한글자씩 센다
3. changeAlpha를 돌리며 제일 앞 글자가 맞는지 확인 아니면 앞글자 다음 글자로 리셋
'''
cnt = 0
changeAlpha = {
    'c':['c=','c-'],
    'd':['dz=','d-'],
    'l':['lj'],
    'n':['nj'],
    's':['s='],
    'z':['z=']}
words = list(input())
idx = 0
while idx < len(words):
    if words[idx] in changeAlpha.keys():
        for c in changeAlpha[words[idx]]:
            for j in range(1,len(c)):
                if idx + j >= len(words):
                    break
                elif words[idx+j] != c[j]:
                    break
            else:
                cnt += 1
                idx += len(c)
                break
        else:
            cnt += 1
            idx += 1
    else:
        cnt += 1
        idx += 1
print(cnt)