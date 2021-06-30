'''
수빈 현재 점(N), 동생(K)
수빈 위치 X 걷는다면 X+1, X-1 이동, 순간이동 2X
수빈이가 동생을 찾을 수 있는 가장 빠른 시간 몇 초 후

풀이(BFS)
1. 수빈의 위치 X에서 X+1, X-1, 2X로 이동 후 q에 담기
2. dist기록, 그전 기록이 있으면 return
3. K에 도달했을때 dist출력
4. 개수도 출력해야되니까 같은 초수도 세기
'''
import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    answer = 0
    q = deque()
    q.append(N)
    dist[N] = 1
    while q:
        p = q.popleft()
        if p == K:
            answer += 1
        for next in (p+1,p-1,2*p):
            if next < 0 or next >= 2*MAX:
                continue
            if dist[next] and dist[next] < dist[p] + 1:
                continue
            dist[next] = dist[p] + 1
            q.append(next)
    print(dist[K]-1)
    print(answer)
    return

N,K = map(int,input().split())
MAX = max(N,K)
dist = [0 for _ in range(2*MAX)]
BFS()
