'''
적록색약 빨간색, 초록색 차이를 거의 느끼지 못함
R(빨강), G(초록), B(파랑)
상하좌우로 같은색상이 인접해 있으면 같은 구역에 속함(색상의 차이를 느끼지 못하는 경우 같은 영역이라 함)
1. 배열을 입력 받는다.
2. DFS로 보고, 적록색약이 아닌경우, 색이 다를 떄 cnt를 +1해줌
3. 적록색약인 경우, 빨간색이나 초록색일때 다음 색이 빨간색이나 초록색이면 두 색을 같은 색으로 판단한다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# di = [0,1,0,-1]#우하좌상
# dj = [1,0,-1,0]
# def DFS(i,j,color,blindness):
#     global normal, blindCnt
#     visited[i][j] = True
#     for d in range(4):
#         ni = i + di[d]
#         nj = j + dj[d]
#         if ni < 0 or ni >= N or nj < 0 or nj >= N:
#             continue
#         if visited[ni][nj]:
#             continue
#         if color != arr[ni][nj]:
#             # 적록색약인 경우
#             if blindness and (color in colorList and arr[ni][nj] in colorList):
#                 DFS(ni,nj,arr[ni][nj],blindness)
#             else:
#                 continue
#         DFS(ni, nj, arr[ni][nj], blindness)
#
#
# N = int(input())
# arr = [list(input()) for _ in range(N)]
#
# visited = [[False for j in range(N)] for i in range(N)]
# colorList = ['R','G']
# normal = 0
# blindCnt = 0
#
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             # 적록색약인경우
#             blindCnt += 1
#             DFS(i,j,arr[i][j],True)
# visited = [[False for j in range(N)] for i in range(N)]
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             # 아닌경우
#             normal += 1
#             DFS(i,j,arr[i][j],False)
# print(normal,blindCnt)

'''
적록색약은 배열을 받을 때 G를 R로 바꿔줌
'''
di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def DFS(i,j,color,arr):
    visited[i][j] = True
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if visited[ni][nj]:
            continue
        if color != arr[ni][nj]:
            continue
        DFS(ni, nj, arr[ni][nj], arr)
N = int(input())
normalArr, blindArr = [['' for j in range(N)] for i in range(N)],[['' for j in range(N)] for i in range(N)]
for i in range(N):
    temp = list(input())
    for j in range(N):
        normalArr[i][j] = temp[j]
        if temp[j] == "G":
            blindArr[i][j] = "R"
        else:
            blindArr[i][j] = temp[j]
visited = [[False for j in range(N)] for i in range(N)]
normalCnt, blindnessCnt = 0,0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            normalCnt+=1
            DFS(i,j,normalArr[i][j],normalArr)

visited = [[False for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            blindnessCnt+=1
            DFS(i,j,blindArr[i][j],blindArr)
print(normalCnt,blindnessCnt)