'''
1. 빈 배열을 만들어준다(M행 N열)
2. 직사각형 좌표를 입력받고 빈 배열에 -1로 표시해준다
3. dfs 함수를 만들고 상하좌우를 살펴보며 방문하지 않았고,값이 0인 것에 사각형 개수번호를 입력해준다.
'''
import sys
sys.setrecursionlimit(10**8)
di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def DFS(i,j):
    global cnt
    arr[i][j] = cnt
    visited[i][j] = True
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= M or nj < 0 or nj >= N:
            continue
        if visited[ni][nj]:
            continue
        if arr[ni][nj] == -1:
            continue
        DFS(ni,nj)


M,N,K = map(int,input().split())
arr = [[0 for j in range(N)] for i in range(M)]
visited = [[False for j in range(N)] for i in range(M)]
cnt = 0
for k in range(K):
    #왼쪽위 꼭지점, 오른쪽 아래 꼭지점
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = -1

for i in range(M):
    for j in range(N):
        if not visited[i][j] and not arr[i][j]:
            cnt += 1
            DFS(i,j)

print(cnt)
ans = [0]*cnt
for i in arr:
    for c in range(1,cnt+1):
        ans[c-1] += i.count(c)
print(*sorted(ans))