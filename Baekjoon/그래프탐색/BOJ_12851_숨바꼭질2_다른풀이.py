from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

# N이 K보다 크면 -1로만 적용
if N >= K:
    print(N-K)
    print(1)
else:
    cnt = 0 #최소거리 경우의수 변수
    MIN = 100001 #최소거리 초기값
    visited = [False for _ in range(MIN)]
    q = deque() # 현위치, dist
    q.append((K,0))
    while q:
        pos, dist = q.popleft() # 현위치, 거리
        visited[pos] = True # 현위치 방문처리

        # dist가 MIN보다 커지면 더이상 볼 필요 없음
        if dist > MIN:
            continue
        # 위치가 N에 도달하면
        if pos == N:
            # dist가 MIN보다 작으면 갱신, 같다면 cnt+1
            if dist < MIN:
                MIN = dist
                cnt = 1
            elif dist == MIN:
                cnt += 1
        else:
            # pos가 짝수고 방문안했다면 //2
            if not pos % 2 and not visited[pos//2]:
                q.append((pos//2,dist+1))
            # pos가 범위에서 벗어나지 않고 방문안했다면 +1,-1
            if 0 <= pos - 1 and not visited[pos-1]:
                q.append((pos-1,dist+1))
            if pos + 1 <= 100000 and not visited[pos+1]:
                q.append((pos+1,dist+1))
    print(MIN)
    print(cnt)
