'''
+와 -에 적절히 괄호를 써서 최소값을 만들어라
1. 식을 입력받는다.
2. + 또는 -를 기준으로 리스트에 각각 담는다.
3. 덧셈끼리 모두 묶은 뒤 더하고, 뺴기
'''
arr = input().split('-')
answer = 0
# 마이너스 앞의 수를 다 더해줌
for i in arr[0].split('+'):
    answer += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        answer -= int(j)
print(answer)