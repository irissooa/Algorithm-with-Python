'''
1. 배열을 입력받는다
2. DFS 이용해 푼다.
3. 배열을 보면서 상하좌우 중 한 곳을 가는데 이미 이동한 동일한 알파벳은 못지나감
4. 최대 몇칸
'''
import sys
from collections import deque

input = sys.stdin.readline
di = [0,1,0,-1] #우하좌상
dj = [1,0,-1,0]
def DFS(pi,pj,go,cnt):
    global MAX
    if MAX < cnt:
        MAX = cnt
    for d in range(4):
        ni = pi + di[d]
        nj = pj + dj[d]
        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            continue
        if arr[ni][nj] in go:
            continue
        go.append(arr[ni][nj])
        DFS(ni,nj,go,cnt+1)
        go.pop()

def BFS(q):
    global MAX
    while q:
        pi,pj,go = q.pop()
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                continue
            if arr[ni][nj] in go:
                continue
            q.append((ni,nj,go+arr[ni][nj]))
            MAX = max(MAX, len(go)+1)

def setBFS(i,j):
    global MAX
    q = set()
    q.add((i,j,arr[i][j]))
    while q:
        pi,pj,go = q.pop()
        MAX = max(MAX,len(go))
        if MAX == 26:
            return
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                continue
            if arr[ni][nj] in go:
                continue
            q.add((ni,nj,go+arr[ni][nj]))
    return
R,C = map(int,input().split( ))
arr = []
for _ in range(R):
    arr.append(list(input()))
MAX = 1
# 1) DFS
# DFS(0,0,[arr[0][0]],1)
# 2) BFS
# go = deque()
# go.append((0,0,arr[0][0]))
# BFS(go)
# 3) set 이용
setBFS(0,0)
print(MAX)
