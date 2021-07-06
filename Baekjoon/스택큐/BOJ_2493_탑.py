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
N = int(input())
top = list(map(int,input().split()))
answer = [0]
post = top[0]
for i in range(1,N):
    if post >= top[i]:
        answer.append(i+1)