'''
정수를 저장하는 스택,
스택은 LIFO(마지막에 들어간것이 먼저나감)
push X : X를 스택에 넣는 연산
pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력, 만약 스택에 들어있는 정수가 없는 경우 -1 출력
size : 스택에 들어있는 정수의 개수 출력
empty : 스택이 비어있으면 1, 아니면 0 출력
top : 스택의 가장 위에 있는 정수 출력, 만약 없으면 -1
'''
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order = input()
    if "push" in order:
        stack.append(int(order[5:]))
    elif "pop" in order:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif "size" in order:
        print(len(stack))
    elif "empty" in order:
        if stack:
            print(0)
        else:
            print(1)
    elif "top" in order:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    #print(order,stack)

