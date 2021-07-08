'''
리스트의 오른쪽부터 왼쪽방향으로 레이저 발사,
출력 : 몇번쨰 탑이 신호를 받는지
1. 리스트를 뒤에서부터 보는데 그앞의 수가 자기보다 같거나 커야 수신받음!, 만약 없다면 0
'''
import sys
input = sys.stdin.readline
'''
# 시간초과
N = int(input())
top = list(map(int,input().split()))
answer = []
for i in range(N-1,-1,-1):
    now = top[i]
    idx = i-1
    ans = 0
    while idx >= 0:
        next = top[idx]
        if now <= next:
            ans = idx + 1
            break
        else:
            idx -= 1
    answer.append(ans)
answer.reverse()
print(*answer)
'''
'''
N = int(input())
top = list(map(int,input().split()))
answer = []
stack = [] #(idx,값) 넣음
for i in range(N):
    while stack:
        # 수신가능
        if stack[-1][1] >= top[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    # 스택이 비면 수신할 탑이 없다.
    if not stack:
        answer.append(0)
    stack.append([i,top[i]])
print(" ".join(map(str,answer)))
'''
# 다른코드
def deep(idx,num):
    if idx == 0:
        return 0
    if top[idx] >= num:
        return idx
    else:
        return deep(result[idx],num)

N = int(input())+1
top = list(map(int,input().split()))
top.insert(0,0)
result = [0]*N
for i in range(2,N):
    if top[i-1] > top[i]:
        result[i] = i-1
    else:
        result[i] = deep(result[i-1],top[i])
print(' '.join(map(str,result[1:])))