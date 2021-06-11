'''
1. 7명의 여학생으로 구성
2. 강한 결속력 위해, 7명의 자리는 서로 가로나 세로로 반드시 인접
3. 반드시 이다솜파(S) 학생들로만 구성될 필요 없다
4. 그러나 이다솜파(S)가 적어도 4명이상
모든 경우의수 출력

S(이다솜)파 , Y(임도연파) 5줄
1. DFS(i,j,group)으로 한 뒤 방문은 찾을때마다 리셋(set으로 좌표를 넣을 예정)
2. group에는 S,Y와 좌표를 추가하는데 만약 Y가 4개이상이면 더이상 Y를 넣지 못함
3. 결과도 set으로 하고 group을 정렬해서 중복되지 않게 넣는다.
'''
import sys
input = sys.stdin.readline

di = [0,1,0,-1] #우하좌상
dj = [1,0,-1,0]
def DFS(group,cnt,Ycnt):
    global result
    if Ycnt > 3:
        return
    if cnt == 7:
        group.sort()
        # print(group)
        result.add(tuple(group))
    else:
        adj = []
        for p in range(len(group)):
            for d in range(4):
                ni = group[p][0] + di[d]
                nj = group[p][1] + dj[d]
                if ni < 0 or ni >= 5 or nj < 0 or nj >= 5:
                    continue
                if (ni,nj) in group:
                    continue
                adj.append((ni,nj))
        for a in adj:
            nexti = a[0]
            nextj = a[1]
            if arr[nexti][nextj] == "S":
                DFS(group + [(nexti,nextj)],cnt+1,Ycnt)
            else:
                DFS(group + [(nexti,nextj)],cnt+1,Ycnt+1)




arr = [list(input()) for _ in range(5)]
result = set()
for i in range(5):
    for j in range(5):
        if arr[i][j] == "S":
            DFS([(i,j)],1,0)

print(len(result))

'''
SSSSS
SSSSS
SSSSS
SSSSS
SSSSS
'''