'''
|r1-r2| + |c1-c2| = 1이면 인접하다고 함
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정함
2. 1을 만족하는 칸이 여러개면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
3. 2를 만족하는 칸도 여러개면 행의 번호가 가장 작은 칸,
4. 그러한 칸도 여러개면 열의 번호가 가장 작은 칸
모두 배치한 다음 학생의 만족도 총합을 구함
만족도는 10 ** 좋아하는 학생의 수로 합을 더하면 된다.

구현
1. 학생들 차례로 자리를 배정
2. 딕셔너리로 key(학생번호), value(좋아하는 학생 리스트) 받음
3. 비어있는 칸 중 인접한칸(상하좌우대각선 8방향)을 살펴보고 좋아하는 번호가 많은 칸을 고름
3-1. 만약 여러개다, 인접한 칸 중 비어있는 칸이 가장 많은칸
3-2. 이것도 여러개면 행의번호 가장 작은칸
3-3. 여러개면 열의 번호 가장 작은 칸
=> 해당 배열의 dist배열을 추가로 만들어 방문기록(인접칸 좋아하는 번호수, 빈칸수, 행번호, 열번호)
1) bfs 함수 만듦(8방향)
2) 빈칸을 큐에 넣고 시작
3) for문으로 8방향 돌면서(범위벗어난것 제외) 인접한칸 좋아하는 번호 수를 세고, 빈칸수 세고, 행번호, 열번호와 함께 []에 기록
4) 모두 센뒤, dist배열을 돌면서 인접한 칸 좋아하는 번호수 많은 것 찾기 -> 빈칸수 많은거 ->행작은거 -> 열작은거
4. 모두 배치 후 좋아하는 학생 수만큼 10의 제곱수로 더함
'''
import sys
from collections import deque
sys.stdin = open('input.txt','r')

di = [0,1,0,-1,-1,-1,1,1]#우하좌상 좌상대 좌하대 우상대 우하대
dj = [1,0,-1,0,-1,1,-1,1]
def bfs(s):
    q = deque()
    q.append([s,students[s]])
    while q:
        student,likeList = q.popleft()
        likecnt,blankcnt = 0,0
        for i in range(N**2):
            for j in range(N**2):
                if arr[i][j]:
                    continue
                for d in range(8):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if ni < 0 or ni >= N or nj < 0 or nj >= N:
                        continue
                    if arr[ni][nj]:
                        if arr[ni][nj] in likeList:
                            likecnt += 1
                        continue
                    if not arr[ni][nj]:
                        blankcnt += 1
                        continue

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    students = {}
    for _ in range(N**2):
        s = list(map(int,input().split()))
        students[s[0]] = s[1:]
    arr = [[0 for j in range(N**2)] for i in range(N**2)]
    for i in students:
        bfs(i)