'''
크기가 NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램 작성
퀸은 가로,세로,대각선 8방향을 움직일 수 있다.
행과열을 저장해야 하기때문에 이중리스트를 사용할려 했는데 리스트 한개만으로 행과열을 표현할 수 있다.
row라는 리스트가 있다고 할때 row에 index값들을 행으로 보고 row[index]의 값을 열로 나타내면 된다.
1. N을 입력받는다.
2. dfs와 check(갈수있는지 확인하는 함수)이용,
1) 같은 행인지 확인 : for문을 돌릴때 x전까지 돌리기 때문에 i와 x가 같을 일은 없기때문에 같은 행에 놓을 수는 없기 때문에 조건문에 안넣어도 된다.
2) 같은 열인지 확인 : 열을 확인해주기 위해서 row[x]와 row[i]를 비교해줘서 같은경우 놓을 수 없기 때문에 false를 준다.
3) 같은 대각선상 인지 확인 : 대각선을 확인하는데 같은 대각선상에 있다는 뜻은 행끼리 뺀 값과 열끼리 뺸 값이 같으면 대각선상에 있다는 뜻이다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check(idx):
    for i in range(idx):
        # 같은 열인지 확인
        if chess[idx] == chess[i] or (abs(chess[idx] - chess[i]) == idx - i):
            return False
        # 같은 대각선인지 확인, # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
        # elif abs(chess[idx] - chess[i]) == idx - i:
        #     return False
    return True

def DFS(idx):
    global pos
    if idx == N:
        pos += 1
        return
    else:
        #각 행에 퀸 놓기
        for i in range(N):
            # i 는 열번호 0부터 N-1까지
            chess[idx] = i
            # 행, 열, 대각선 체크함수 true면 가능
            if check(idx):
                DFS(idx+1)

N = int(input())
chess = [0] * N
pos = 0
DFS(0)
print(pos)