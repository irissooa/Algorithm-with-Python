'''
( )로 이루어진 문자열
올바른 괄호 문자열(VPS) 판단
1. 입력받는다
2. ( 여는 괄호를 스택에 넣는다. )닫는 괄호가 나올때까지 넣는다.
3. 닫는 괄호가 나온다면 스택에 넣은 괄호중 제일 뒤에 것 빼서 짝이 맞는지 확인
4. 안맞다면 NO 출력, 맞다면 YES
'''
T = int(input())
for tc in range(1,T+1):
    parenthesis = list(input())
    stack = []
    for p in parenthesis:
        if p == "(":
            stack.append(p)
        # 닫는 괄호를 만남
        elif p == ")" and stack:
            close = stack.pop()
        else:
            print("NO")
            break
    else:
        if stack:
            print("NO")
        else:
            print("YES")