'''
수빈 현재 점(N), 동생(K)
수빈 위치 X 걷는다면 X+1, X-1 이동, 순간이동 2X
수빈이가 동생을 찾을 수 있는 가장 빠른 시간 몇 초 후

풀이(BFS)
1. 수빈의 위치 X에서 X+1, X-1, 2X로 이동 후 q에 담기
2. dist기록, 그전 기록이 있으면 return
3. K에 도달했을때 dist출력
'''
import sys
input = sys.stdin.readline
from collections import deque


def BFS(q):
    dist[N] = 1
    while q:
        n = q.popleft()
        if n == K:
            break
        for next in (n-1,n+1,2*n):
            if next < 0 or next >= 100001:
                continue
            if dist[next]:
                continue
            dist[next] = dist[n] + 1
            q.append(next)


N, K = map(int,input().split())
q = deque()
dist = [0 for _ in range(100001)]
q.append(N)
BFS(q)
print(dist[K]-1)

'''
수빈 현재 점(N), 동생(K)
수빈 위치 X 걷는다면 X+1, X-1 이동, 순간이동 2X
수빈이가 동생을 찾을 수 있는 가장 빠른 시간 몇 초 후

풀이(재귀)
1.n이 k보다 크면 n-k로 그 차를 반환
2. k==1이면 1반환
3. k가 홀수면 n과 k-1, n과 k+1로 다시 check 돌린 것의 min값에 1 더한값 리턴
4. 그외에는 k-n(k가 더 크기때문)과 1+check(n,k//2)한 것의 최소값,
'''
import sys
input = sys.stdin.readline

def check(n,k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k % 2:
        return 1+min(check(n,k-1),check(n,k+1))
    else:
        return min(k-n,1+check(n,k//2))


N,K = map(int,input().split())
MAX = max(N,K)
print(check(N,K))
