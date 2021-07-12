# BAEKJOON_DFS,BFS

[toc]

## 목차

1. [11724_연결요소의 개수](#11724_연결요소의-개수)
2. [5667_결혼식](#5667_결혼식)
3. [2644_촌수계산](#2644_촌수계산)
4. [SWEA_5521_상원이의생일파티](#SWEA_5521_상원이의생일파티)
5. [9466_텀프로젝트](#9466_텀프로젝트)
6. [5639_이진검색트리](#5639_이진검색트리)
7. [10451_순열사이클](#10451_순열사이클)
8. [1991_트리순회](#1991_트리순회)
9. [11725_트리의 부모찾기](#11725_트리의-부모찾기)
10. [4963_섬의개수](#4963_섬의개수)
11. [2331_반복수열](#2331_반복수열)
12. [SWEA_5188_최소합](#SWEA_5188_최소합)
13. [BOJ_2668_숫자고르기](#BOJ_2668_숫자고르기)
14. [SWEA_5208_전기버스2](#SWEA_5208_전기버스2)
15. [BOJ_2468_안전영역](#BOJ_2468_안전영역)
16. [BOJ_5014_스타트와링크](#BOJ_5014_스타트와링크)
17. [BOJ_9205_맥주마시면서걸어가기](#BOJ_9205_맥주마시면서걸어가기)
18. [BOJ_2573_빙산](#BOJ_2573_빙산)
19. [BOJ_2583_영역구하기](#BOJ_2583_영역구하기)
20. [BOJ_1987_알파벳](#BOJ_1987_알파벳)
21. [BOJ_10026_적록색약](#BOJ_10026_적록색약)
22. [BOJ_1941_소문난칠공주](#BOJ_1941_소문난칠공주)
23. [프로그래머스_타겟넘버](#프로그래머스_타겟넘버)
24. [프로그래머스_네트워크](#프로그래머스_네트워크)
25. [프로그래머스_단어변환](#프로그래머스_단어변환)
26. [프로그래머스_여행경로](#프로그래머스_여행경로)
27. [BOJ_1697_숨바꼭질](#BOJ_1697_숨바꼭질)
28. [BOJ_12851_숨바꼭질2](#BOJ_12851_숨바꼭질2)
29. [프로그래머스49189가장 먼노드](#프로그래머스49189가장 먼노드)

## 11724_연결요소의 개수

> 처음에  DFS로 풀었을 떄 런타임 에러가 났다ㅠㅠㅠ 그래서 bfs로도 풀어봤는데 런타임에러가 났다
>
> 질문검색으로 찾아보니까 `sys.setrecursionlimit(10**6)`를 써서 재귀 깊이를 늘려주는게 하나의 방법이라고 했다!

```python
'''
소요시간 : 2020/10/25/10:05
방향없는 그래프 -> 인접리스트에 표시
첫째줄부터 연결 요소의 개수를 출력!
dfs하면 될듯
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
sys.setrecursionlimit(10**6)

#근데...런타임에러ㅠ하..bfs로도 해보자
def DFS(s):
    #방문했으니 방문표시
    visited[s] = True
    #인접리스트에 있고, 방문하지 않은 정점이라면
    for e in arr[s]:
        if not visited[e]:
            DFS(e)

def BFS(s):
    q=[s]
    while q:
        p = q.pop()
        for e in arr[p]:
            if not visited[e]:
                visited[e] = True
                q.append(e)


#정점의 개수N,간선의 개수M
N,M = map(int,sys.stdin.readline().split())
#인접리스트
arr = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    #간선의 양 끝점 u,v주어짐
    u,v = map(int,sys.stdin.readline().split())
    #무방향이니까 둘다 표시해줌
    arr[u].append(v)
    arr[v].append(u)
cnt = 0 #연결요소를 세어줌
for s in range(1,N+1):
    if not visited[s]:
        DFS(s)
        # BFS(s)
        cnt += 1
# pprint(arr)
print(cnt)
```



## 5667_결혼식

```python
'''
6
5
1 2
1 3
3 4
2 3
4 5

#1.입력받고, 인접리스트를 만듦.

#2.BFS(1)로 출발
    이 프로그램은 친구 한명한명당 상근이와 얼마나 떨어져있는지 dist를 계산해줌
    => dist[] 있어야함
#3.그리고 프로그램 끝나면 dist에 다 추가 되있어야 함. dist의 value가 2인것만그 개수를 세줌
'''

import sys
sys.stdin = open('input.txt','r')
from collections import deque

def BFS(s):
    invite.append(s)
    while invite:
        ps = invite.popleft()
        for pe in friends[ps]:
            #0이아니면 방문!
            if dist[pe]:
                continue
            #아니라면 invite에 넣어줌
            dist[pe] = dist[ps] +1
            invite.append(pe)

#상근이 동기의 수n,
n = int(input())
#m 리스트 길이
m = int(input())
friends = [[]*(n+1) for _ in range(n+1)]
dist = [0]*(n+1)
invite = deque()
for _ in range(m):
    #친구관계
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)
BFS(1)
# print(dist)
cnt = 0
for i in range(2,n+1):
    if 0 < dist[i] <=2:
        cnt+=1
print(cnt)
```



## 2644_촌수계산

```python
'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
부모와 자식 사이 1촌
주어진사람들 촌수 구하기
#1. parent idx list에 child를 append(양방향으로!!)
#2. BFS(s)를 한뒤 구하고자하는 e까지 bfs돌리고 dist+=1추가해서 몇촌인지 구하기
'''
from collections import deque
def BFS(start):
    R.append(start)
    while R:
        ps = R.popleft()
        if ps == e:
            return
        for pe in family[ps]:
            if dist[pe]:
                continue
            dist[pe] = dist[ps] + 1
            R.append(pe)

#전체 사람 수
n = int(input())
#촌수 계싼해야되는 두 사람의 번호
s,e = map(int,input().split())
#부모 자식들 간의 관계의 개수
m = int(input())
family = [[0]*(n+1) for _ in range(n+1)]
dist = [0]*(n+1)
R = deque()
for _ in range(m):
    parent, child = map(int,input().split())
    family[parent].append(child)
    family[child].append(parent)
BFS(s)
if dist[e]:
    print(dist[e])
else:
    print(-1)
```



## SWEA_5521_상원이의생일파티

```python
'''
친구관계 리스트를 양방향으로 인접리스트에 담아줌
dist를 써서 bfs, 거리가 2이내인 개수 세주기
'''
import sys
sys.stdin = open('input.txt','r')

def BFS(v):
    q = [v]
    while q:
        p = q.pop(0)
        for n in friends[p]:
            if dist[n]:
                continue
            dist[n] = dist[p]+1
            q.append(n)

T = int(input())
for tc in range(1,T+1):
    #N은 상원이 반 친구들, M은 친한관계수
    N,M = map(int,input().split())
    friends = [[] for i in range(N+1)]
    for m in range(M):
        #a와 b는 친한관계
        a,b = map(int,input().split())
        friends[a].append(b)
        friends[b].append(a)
    # print(friends)
    dist = [0 for i in range(N+1)]
    BFS(1)
    # print(dist)
    cnt = 0
    for d in range(2,N+1):
        if 0 < dist[d] <= 2:
            cnt+=1
    print('#{} {}'.format(tc,cnt))
```



## 9466_텀프로젝트

> [9466_텀프로젝트](https://www.acmicpc.net/problem/9466)

- 이렇게 푸니까 재귀로 계속 돌려서 그런지 시간초과가 났다...ㅠ 재귀말고 다르게 풀어야될것 같다...

```python
import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**8)

def DFS(node):
    global cnt
    #q리스트 안에 node값이 이미 있다면 어딘가는 반복된다는 것! 그 값부터 한팀! 그전의 값들은 방문표시안함
    if node in q:
        #q안의 node들 모두 방문표시, 다시 못가게
        for i in q:
            visited[i] = 1
        #어느 위치가 반복되는지 찾고, 그 위치부터는 쭉 cnt를 표시해줌
        idx = q.index(node)
        for p in range(idx,len(q)):
            cnt+=1
        return
    #q안에 node값이 없다면 일단 q에 넣어줌
    q.append(node)
    #그 node의 값이 방문하지 않았다면 info[node]로 DFS돌림
    if not visited[info[node]]:
        DFS(info[node])

T = int(input())
for tc in range(1,T+1):
    #학생의 수
    N = int(input())
    #index를 맞추기 위해 앞에 0 삽입
    info = [0]+list(map(int,input().split()))
    visited = [0 for _ in range(N+1)]
    cnt = 0
    #자기자신을 가리키는 node는 방문처리
    for i in range(1,N+1):
        if i == info[i]:
            visited[i] = 1
            cnt += 1
    for i in range(1,N+1):
        q = []#잠시 팀원들을 담을 리스트
        if not visited[i]:
            DFS(i)
    print(N-cnt)
```



- 쥬아's code

```python
# 전체 - 팀을 이룰 수 있는것 이렇게 구하자

def DFS(v):
    global passed
    global dfsPath

    # 만약에 v가 dfsPath에 있으면 그 위치부터 반복됨
    if v in dfsPath:
        # 팀에 못끼는 애나 팀된애들이나 이제 접근하면 안되므로 방문처리
        for i in dfsPath:
            visited[i] = 1
        # 반복의 시작부터 끝까지 개수 세주기
        # 반복 아닌 부분은 세면 안되니까
        for i in range(len(dfsPath)):
            if dfsPath[i] == v:
                for j in range(i, len(dfsPath)):
                    passed += 1
        # for i in range(p,len(dfsPath)):
        #     passed += 1
        return
    # 일단 넣어주고
    dfsPath.append(v)

    # 다음놈이 접근가능하면 DFS돌리기
    if visited[team[v]] == 0:
        DFS(team[v])

for T in range(1, int(input())+1):
# for T in range(1, 2):
    N = int(input())
    team = [0] + list(map(int, input().split()))
    visited = [0]*(N+1)

    # 팀플가능한애들 수
    passed = 0
    # 혼자 노는 애있으면 팀플가능수에 넣고 접근못하게 하자
    for i in range(1, N+1):
        if team[i] == i:
            visited[i] = 1
            passed += 1
    # for i in range(1, N+1):


    for i in range(1, N+1):
        dfsPath = []
        if visited[i] == 0:
            DFS(i)

    print(N-passed)
```



- DFS로 풀지않고 반복문으로만 푼 사람을 구글링으로 찾았다...

> [jjangsungwon참고](https://jjangsungwon.tistory.com/40)
>
> - 1번부터 N번까지 순서대로 탐색을 시작한다.
> - 해당 번호에서 **DFS 탐색**을 시작한다. (**지나간 부분은 같은 팀으로 가정**)
> - 위에서 탐색한 방향의 역순으로 탐색하면서 사이클을 확인한다. **(-1을 대입)**
> - **역순으로 탐색**하면서 -1로 채워지지 않은 부분은 팀을 이루지 못한 것이라고 생각하면 된다.

```python
import sys

sys.setrecursionlimit(10 ** 6)


if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        N = int(input())
        p = list(map(int, input().split()))
        p.insert(0, 0)  # 인덱스 편의를 위해서 삽입
        team = [0] * (N + 1)

        for i in range(1, N + 1):
            if team[i] == 0:  # 아직 팀이 없는 경우
                team_number = i
                # 팀 구성한다고 가정
                while team[i] == 0:
                    team[i] = team_number
                    i = p[i]
                # 역순으로 순환하면서 사이클 확인
                while team[i] == team_number:
                    team[i] = -1
                    i = p[i]
        result = N - team.count(-1)
        print(result)
```

- DFS로 풀어서 맞은 코드

> 이분깔끔하게 잘 풀었따....부럽...

```python
import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]
    
    if visited[number]: #방문가능한 곳이 끝났는지
        if number in cycle: #사이클 가능 여부
            result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸
        return
    dfs(number)

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N #방문 여부
    result = []
    
    for i in range(1, N+1):
        if not visited[i]: #방문 안한 곳이라면
            cycle = []
            dfs(i) #DFS 함수 돌림
            
    print(N - len(result)) #팀에 없는 사람 수
```

## 5639_이진검색트리

이거다음에 다시하기ㅠㅠ

>[5639_이진검색트리](https://www.acmicpc.net/problem/5639)
>
>[이진검색트리개념](https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/)
>
>```python
>class Node:
>def __init__(self, val):
>   self.val = val
>   self.leftChild = None
>   self.rightChild = None
>
>def get(self):
>   return self.val
>
>def set(self, val):
>   self.val = val
>   
>def getChildren(self):
>   children = []
>   if(self.leftChild != None):
>       children.append(self.leftChild)
>   if(self.rightChild != None):
>       children.append(self.rightChild)
>   return children
>   
>class BST:
>def __init__(self):
>   self.root = None
>
>def setRoot(self, val):
>   self.root = Node(val)
>
>def insert(self, val):
>   if(self.root is None):
>       self.setRoot(val)
>   else:
>       self.insertNode(self.root, val)
>
>def insertNode(self, currentNode, val):
>   if(val <= currentNode.val):
>       if(currentNode.leftChild):
>           self.insertNode(currentNode.leftChild, val)
>       else:
>           currentNode.leftChild = Node(val)
>   elif(val > currentNode.val):
>       if(currentNode.rightChild):
>           self.insertNode(currentNode.rightChild, val)
>       else:
>           currentNode.rightChild = Node(val)
>
>def find(self, val):
>   return self.findNode(self.root, val)
>
>def findNode(self, currentNode, val):
>   if(currentNode is None):
>       return False
>   elif(val == currentNode.val):
>       return True
>   elif(val < currentNode.val):
>       return self.findNode(currentNode.leftChild, val)
>   else:
>       return self.findNode(currentNode.rightChild, val)
>```
>
>



- [다른 사람 코드](https://developmentdiary.tistory.com/442) -> 트리를 class로 풀었따.. 신기...공부하쟈

> 이렇게 코드를 구현하면 시간초과가 난다.
>
> 이진트리를 만드는데 O(NlogN)
>
> 후위순회를 하는데 O(NlogN)의 시간이 든다.
>
> 트리를 만들지 않고 바로 출력하는 방식으로 만들어야겠다.
>
> 이진트리의 전위순회를 살펴보면
>
> 첫번째 루트 노드를 기준으로 작은값은 왼쪽 큰값은 오른쪽으로 나뉘는것을 볼 수 있다.
>
> 50 / 30 24 5 28 / 45 98 52 60
>
> 이렇게 분할하여 문제를 해결할수있다.

```python
class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None
 
 
class BinaryTree:
    def __init__(self):
        self.head=Node(None)
 
 
    def insert(self,item):#루트존재여부 확인
        if self.head.val is None:
            self.head.val = item
        else:
            self.addnode(self.head,item)
 
    def addnode(self,cur,item):
        if cur.val>item:#새로운 인자가 현재보다 작다면 왼쪽
            if cur.left!=None:#왼쪽이 비어있지않다면
                self.addnode(cur.left,item)
            else:#비어있다면 넣어준다.
                cur.left=Node(item)
        elif cur.val<item:#새로운 인자가 현재보다 크다면 오른쪽
            if cur.right!=None:
                self.addnode(cur.right,item)
            else:
                cur.right=Node(item)
    def postorder(self,cur):#후위순회
        if cur.left != None:
            self.postorder(cur.left)
        if cur.right != None:
            self.postorder(cur.right)
        print(cur.val)
 
 
import sys
sys.setrecursionlimit(10**9)
 
 
b_tree=BinaryTree()#초기화
count = 0
while count <= 10000:
    try:
        num = int(input())
    except:break
    b_tree.insert(num)
    count += 1
 
b_tree.postorder(b_tree.head)
```

- 이사람이 고친 코드

```python
def postorder(start,end):
    if start>end:
        return
 
    division=end+1#나눌위치
    for i in range(start+1,end+1):
        if post[start]<post[i]:
            division=i
            break
 
    postorder(start+1,division-1)#분할 왼쪽
    postorder(division,end)#분할 오른쪽
    print(post[start])
 
 
 
import sys
sys.setrecursionlimit(10**9)
 
 
post=[]
count = 0
while count <= 10000:
    try:
        num = int(input())
    except:break
    post.append(num)
    count += 1
 
postorder(0,len(post)-1)
```



## 10451_순열사이클

> [10451_순열사이클](https://www.acmicpc.net/problem/10451)

```python
'''
node의 idx -> node[idx]으로 그래프가 이어짐
dfs로  이어진 node들의 개수를 구하기!
'''

import sys
sys.stdin = open('input.txt','r')


def DFS(s):
    visited[s] = True
    e = node[s]
    if not visited[e]:
        DFS(e)


T =int(input())
for tc in range(1,T+1):
    #순열의크기N
    N = int(input())
    #순열, index맞춰줌
    node = [0]+ list(map(int,input().split()))
    visited = [False for _ in range(N+1)]
    cnt = 0
    for idx in range(1,N+1):
        if not visited[idx]:
            DFS(idx)
            cnt+=1
    print(cnt)
```



## 1991_트리순회

> [1991_트리순회](https://www.acmicpc.net/problem/1991)

```python
'''
전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
이거를 함수로 만든 뒤
전위순회
중위순회
후위순회순으로 출력
'''
import sys
sys.stdin = open('input.txt','r')

def preorder(n):
    print(node[n],end='')
    if L[n] != '.':
        preorder(node.index(L[n]))
    if R[n] != '.':
        preorder(node.index(R[n]))


def inorder(n):
    if L[n] != '.':
        inorder(node.index(L[n]))
    print(node[n],end ='')
    if R[n] != '.':
        inorder(node.index(R[n]))


def postorder(n):
    if L[n] !='.':
        postorder(node.index(L[n]))
    if R[n] != '.':
        postorder(node.index(R[n]))
    print(node[n],end='')

#이진트리 노드의 개수
N = int(input())
node = ['']
#왼쪽자식
L = ['']
#오른쪽 자식
R = ['']
for n in range(N):
    alpha,left,right = input().split()
    node.append(alpha)
    L.append(left)
    R.append(right)
# print(node,L,R)
preorder(1)
print()
inorder(1)
print()
postorder(1)
```



## 11725_트리의 부모찾기

> [11725_트리의부모찾기](https://www.acmicpc.net/problem/11725)
>
> 노드의 방향이 정해져 있지 않아서 문제! DFS로 루트번호 1부터 탐색을 하는데 만약 1과 연결돼있고, 방문하지 않은 node라면 자식배열에 1번 idx에 향하는 노드e를 담아주고, e의 부모배열에 s를 넣어줌!
>
> 그리고 출력은 부모만 하면된다
>
> 여기서 문제는 node개수가 10만개까지 주어지기 때문에 `sys.setrecursionlimit(10**10)` 이거를 써줘서 재귀의 깊이를 늘려줌!

```python
'''
노드를 인접리스트로 노드가 향하는 정점에 담는다
그리고 DFS로 루트 1부터 돌림!
'''
import sys
# sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**10)
def DFS(s):
    visited[s] = True
    for e in node[s]:
        if not visited[e]:
            child[s].append(e)
            parent[e] = s
            DFS(e)

#노드의 개수
N = int(input())
node = [[] for _ in range(N+1)]
child = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    node[s].append(e)
    node[e].append(s)
# print(node)
visited = [False for _ in range(N+1)]
DFS(1)
for p in range(2,N+1):
    print(parent[p])
# print(parent)
```



## 4963_섬의개수

> [4963_섬의개수](https://www.acmicpc.net/problem/4963)
>
> 이거도 재귀에러!
>
> 계산해서 재귀가 1000번 넘어갈것 같으면 `sys.setrecursionlimit(10**6)`이거 쓰기

```python
'''
정사각형으로 이루어진 섬과 바다
섬의 개수를 세는 프로그램
가로,세로,대각선 방향 이동 가능 -> 8방향델타
dfs로 붙어있는 섬의 개수 출력
'''
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
sys.setrecursionlimit(10**6)

di =[0,1,0,-1,-1,1,-1,1]#우하좌상 우상대 우하대 좌상대 좌하대
dj = [1,0,-1,0,1,1,-1,-1]
def DFS(i,j):
    visited[i][j] = True
    for d in range(8):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue
        if visited[ni][nj]:
            continue
        if not MAP[ni][nj]:
            continue
        DFS(ni,nj)

while True:
    #지도 너비 w, 높이 h
    w,h = map(int,input().split())
    #입력의 마지막 줄에는 0 두개가 주어짐
    if w == 0 and h == 0:
        break
    MAP = []
    visited = [[False for j in range(w)] for i in range(h)]
    #h개 줄 지도 1:땅,0은바다
    for _ in range(h):
        MAP.append(list(map(int,input().split())))
    print(h,w)
    pprint(MAP)
    num = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1 and not visited[i][j]:
                DFS(i,j)
                num +=1
    print(num)
```



## 2331_반복수열

> [2331_반복수열](https://www.acmicpc.net/problem/2331)

```python
'''
D에 D[0]=A를 넣고 시작
D[n] = D[n-1]의 각 자리 숫자에 P를 곱한뒤 더한 값을 넣고
while문을 돌리는데
종료조건으로 D에 이미 들어간 숫자가 들어가면 break한 뒤 그 숫자의 앞에 있는 숫자들 개수 출력!
'''
import sys
sys.stdin = open('input.txt','r')
A,P = map(int,input().split())
D = [A]
num = 1
flag=False
while True:
    SUM = 0
    #문자열로 바꿔서 각 자리수를 분리시킴
    for n in range(len(str(D[num-1]))):
        SUM += int(str(D[num-1])[n])**P
        # print(SUM)
    #종료조건
    #D에 이미 들어간 숫자가 있다면 break!
    if SUM in D:
        # print(D)
        #D[num]이 D에 들어있는 수 중 앞에 있는걸 찾아서 그 앞의 수 개수를 출력
        for d in range(len(D)):
            if D[d] == SUM:
                print(len(D[:d]))
                flag=True
                break
        if flag:
            break
    #D[n] = D[n-1]의 각 자리 숫자에 P를 곱한뒤 더한값
    D.append(SUM)
    num+=1

```



## SWEA_5188_최소합

> dfs로 풀어야되는데 굳이 bfs로 풀어서.....ㅠ ㅎ ......ㅠ

```python
'''
방문하지 않은, 주변을 보면서 맨 왼쪽에서 오른쪽 아래로 도착하게함! bfs(최소)
dist에 합을 넣음
'''
import sys
sys.stdin = open('input.txt','r')

di = [0,1]#우하
dj = [1,0]
def BFS(i,j):
    dist[i][j] = numbers[i][j]
    q = [(i,j)]
    while q:
        pi,pj = q.pop(0)
        for d in range(2):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            #다음값에 들어갈 합이 현재까지 누적합 + 현재값보다 크다면 굳이 갈필요 없음, pass
            if dist[ni][nj] < dist[pi][pj] + numbers[ni][nj]:
                continue
            
            #누적합 갱신
            dist[ni][nj] = dist[pi][pj] + numbers[ni][nj]
            q.append((ni,nj))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = []
    dist = [[987654321 for j in range(N)] for i in range(N)]
    for n in range(N):
        numbers.append(list(map(int,input().split())))

    # print(numbers)
    BFS(0,0)
    # print(dist)
    print('#{} {}'.format(tc,dist[N-1][N-1]))

```



## BOJ_2668_숫자고르기

- 처음에는 조합으로 풀었다가 값이 너무 커서 시간초과...

```python
'''
조합! 함수사용
#1. first_numbers에서 K를 N에서부터 뒤로 내려오면서 NCk 만큼 뽑고 second_numbers에서도 NCk만큼 뽑는데 두 집합이 같으면 출력!
'''
from itertools import combinations


N = int(input())
first_numbers = [i for i in range(1,N+1)]
second_numbers = []
for n in range(N):
    second_numbers.append(int(input()))
# print(first_numbers)
# print(second_numbers)
flag = False
MAX = 0
for k in range(N,0,-1):
    first = []
    second = []
    cnt = 0
    for i in list(combinations(first_numbers,k)):
        first.append(i)
    for j in list(combinations(second_numbers,k)):
        second.append(j)
    # print(k,first,second)
    for f in first:
        for s in second:
            if set(f) == set(s):
                MAX = k
                flag = True
                print(MAX)
                print(*f,sep='\n')
                break
        if flag:
            break
    if flag:
        break
```

- 그래서 dfs로 풀었더니 됐따! 텀프로젝트와 똑같이 풀었따...

```python
'''
조합! 함수사용
#1. first_numbers에서 K를 N에서부터 뒤로 내려오면서 NCk 만큼 뽑고 second_numbers에서도 NCk만큼 뽑는데 두 집합이 같으면 출력!

#DFS로 풀기
#1.인접리스트를 만드는데, 유향으로 first->second로 만듦! 여기서 만약 양방향이 된다면 cnt!

#idea
#상대배열에 값이 똑같으면 result 넣고, 만약에 N까지 갔는데 내값이 상대 배열에없으면 둘다 지움...
'''
from itertools import combinations

import sys
sys.stdin = open('input.txt','r')

def DFS(num):
    global result
    visited[num] = True
    cycle.append(num)
    next = linked[num]
    # print(num,next)
    if visited[next]:
        if next in cycle:
            result += cycle[cycle.index(next):]
        return
    DFS(next)

#DFS로 풀기
N = int(input())
linked = [0 for _ in range(N+1)]

for n in range(1,N+1):
    linked[n]=int(input())
# print(linked)


result = []
visited = [False for j in range(N+1)]
for i in range(1,N+1):
    if not visited[i]:
        cycle = []
        DFS(i)
        # print(i,visited)
print(len(result))
# print(*result,sep='\n')
for i in sorted(result):
    print(i)

```



## SWEA_5208_전기버스2

> [SWEA_5208_전기버스2](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do#none)

```python
'''
출발지에서의 배터리 장착은 교환횟수에서 제외
앞에서부터 보면서 bfs돌림?
battery에서 해당 idx에 idx값만큼 갈수 있는 곳을 인접리스트에 담음
그리고 bfs돌리며 dist최솟값....ㅎ
'''
import sys
sys.stdin = open('input.txt','r')

def BFS(node):
    q = [node]

    while q:
        p = q.pop(0)
        for i in linked[p]:
            if i == N:
                return
            if dist[i]:
                continue
            dist[i] = dist[p] +1
            q.append(i)



T = int(input())
for tc in range(1,T+1):
    #정류장 수 N,N-1개의 정류장 별 배터리 용량
    info = list(map(int,input().split()))
    N = info[0]
    #종점은 배터리가 없음
    battery = info[1:]+[0]
    # print('b',battery)
    linked = [[] for _ in range(N)]
    for i in range(N):
        linked[i].extend(list(x for x in range(i+1,i+battery[i]+1)))
    # print(linked)
    dist = [0 for _ in range(N)]
    BFS(0)
    #출발점은 cnt안세줄것이기 때문
    print('#{} {}'.format(tc,dist[N-1]-1))
```



## BOJ_2468_안전영역

```python
'''
2020-12-09 19:30-19:50
지역의 높이를 파악하고, 물에 잠기지 않는 안전한 영역이 몇개인지 조사
위아래 오른쪽 왼쪽으로 인접해있는 안전영역 뭉치 개수가 최대가 되는 값

상하좌우 dfs돌면서 뭉치의 개수 최대치 구하기
배열을 받을 때 높이 최소, 최대값 기록해두기
1. 높이 H(최소부터 시작) for문 돌면서 배열값이 높이 H 초과인 것의 뭉치 개수를 델타이용해서 찾기
2. 개수 다 찾은 뒤 최대 갱신하고, H+1해서 다시 찾기
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
INF = sys.maxsize
sys.setrecursionlimit(10**8)

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def DFS(i,j):
    visited[i][j] = True
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if visited[ni][nj]:
            continue
        if arr[ni][nj] <=H:
            continue
        DFS(ni,nj)


N = int(input())
arr = []
maxnum,minnum=-INF,INF
for _ in range(N):
    temp = list(map(int,input().split()))
    if max(temp) > maxnum:
        maxnum = max(temp)
    if min(temp) < minnum:
        minnum = min(temp)
    arr.append(temp)
# for x in arr:
#     print(x)
# print(maxnum,minnum)

MAX = 0
H=minnum-1
while H <= maxnum:
    visited = [[False for j in range(N)] for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > H and not visited[i][j]:
                cnt+=1
                DFS(i,j)
    if cnt > MAX:
        MAX = cnt
    H+=1
print(MAX)
```

- 다른코드

```python
import sys
from collections import defaultdict as dd
input = sys.stdin.readline

def Repr(a):
    if Set[a] == a:
        return a
    k = Repr(Set[a])
    Set[a] = k
    return k

def Join(a,b):
    Set[Repr(b)] = Repr(a)

def adj(p):
    yield p - w
    yield p - 1
    yield p + 1
    yield p + w

n = int(input())
w = n + 2

Set = {}

contour = dd(list)
for i in range(1, n+1):
    new = list(map(int, input().split()))
    for h, j in zip(new, range(i*w+1, (i+1)*w - 1)):
        contour[h].append(j)
heights = sorted(contour, reverse = True)
heights.pop()
fixed = []
cnt = 1
for h in heights:
    for k in contour[h]:
        Set[k]=k
    for p in contour[h]: # Connection change is made from added points(to both new and old components)
        for q in adj(p):
            if q in Set: Join(p, q)
    fixed = [p for p in fixed if Set[p] == p]
    for p in contour[h]:
        if Set[p] == p:
            fixed.append(p)
    cnt = max(cnt, len(fixed))

print(cnt)

```

```python
import sys
sys.setrecursionlimit(20000)
def f(a,v,x,y):
    a[x][y]-=1;v[x][y]=0
    if v[x-1][y]:f(a,v,x-1,y)
    if v[x+1][y]:f(a,v,x+1,y)
    if v[x][y-1]:f(a,v,x,y-1)
    if v[x][y+1]:f(a,v,x,y+1)
n=int(input())+2
a=[[0]*n]+[[0]+[*map(int,i.split())]+[0]for i in sys.stdin]+[[0]*n]
r=[]
for l in range(max([max(i)for i in a])):
    v=[[j for j in i]for i in a];c=0
    for i in range(1,n-1):
        x=v[i]
        for j in range(1,n-1):
            if x[j]:f(a,v,i,j);c+=1
    r+=[c]
print(max(r))
```

```python
import sys
sys.setrecursionlimit(10**6)
a=int(input())
c=[]
c.append([0]*(a+2))
for i in range(a):
     b=list(map(int,input().split()))
     b.insert(0,0)
     b.append(0)
     c.append(b)
c.append([0]*(a+2))
Ans=[]
ans=0
def dfs(x,y,z) :
     global ans
     c[x][y]=z
     if c[x-1][y]>z:
          dfs(x-1,y,z)
     if c[x+1][y]>z:
          dfs(x+1,y,z)
     if c[x][y-1]>z:
          dfs(x,y-1,z)
     if c[x][y+1]>z:
          dfs(x,y+1,z)  
for i in range(101,-1,-1):
     for j in range (1,a+1):
          for k in range(1,a+1):
               if c[j][k]>i :
                    ans+=1
                    dfs(j,k,i)
     if ans==0 :
          continue
     else:
          Ans.append(ans)
          ans=0
print(max(Ans))

```







## BOJ_5014_스타트와링크

> dist[next]가 있으면 지나가게 하니까 시간초과가 나오지 않았따....ㅠ 최소값이니까 당연히 그래야지..ㅠ

```python
'''
2020-12-09 23:40-
F층으로 이루어진 건물, G층으로 가야됨, 강호가 있는 곳은 S층
엘베 버튼 2개밖에 없음 U버튼은 위로 U층을 가는 버튼, D버튼은 밑으로 D층을 가는 버튼, 갔는데 해당 층이 없으면 엘베 안움직임
G층에 도착하려면 최소 몇번 버튼 눌러야 되나
갈수없다면 use the stairs출력

1. F까지의 1차원 dist배열을 만듦
2. S에서 +U만큼, -D만큼 보냄
3. 거기서 범위체크 계속하며 dist최소값 갱신, dist[G-1]-1을 뽑는다 없다면  use the stairs출력
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque


def BFS(node):
    q = deque()
    q.append(node)
    dist[node] = 1
    while q:
        p = q.popleft()
        if p == G:
            return
        for n in [U,-D]:
            next = p + n
            # print(next,p,n)
            if next <= 0 or next > F:
                continue
            # if dist[next] and dist[next] < dist[p] + 1:
            #     continue
            if dist[next]:
                continue
            dist[next] = dist[p] + 1
            if next == G:
                return
            q.append(next)


# 가장높은층 F, 강호위치S층, G층이목표, U위로 올라감,D아래로 내려감
F,S,G,U,D = map(int,input().split())
dist = [0 for _ in range(F+1)]
BFS(S)
ans = dist[G]-1
if S == G:
    print(0)
elif ans >0:
    print(ans)
else:
    print('use the stairs')
# print(dist)
```



- 다른사람코드

```python
import sys
from collections import deque

#sys.stdin = open("input.txt","r")

F, S, G, U, D = tuple(map(int, sys.stdin.readline().rstrip().split()))
time = 0
List = deque()

if G > S and U != 0:
    b = (G-S) // U
    S += b*U
    time = b
elif G <= S and D != 0:
    b = (S-G) // D
    S -= b*D
    time = b

List.append((S,time))

up_down = [U,-D]
visited = [0 for i in range(F+1)]

while List:
    a = List.popleft()
    current = a[0]
    time = a[1]
    if current == G:
        print(time)
        break
    visited[current] = 1

    for i in up_down:
        nextPos = current + i
        if nextPos > F or nextPos < 1:
            continue
        elif visited[nextPos] == 0:
            List.append((nextPos,time+1))

    if len(List) == 0:
        print("use the stairs")
        break

```

```python
import sys
from collections import deque

input = sys.stdin
sys.setrecursionlimit(5000)


def bfs(s, g, f, u, d):
    q = deque()
    q.append((s, 0))
    visited[s] = True
    ans = int(1e9)
    while q:
        here, dist = q.popleft()
        if here == g:
            ans = dist
            break
        nx1 = here + u
        nx2 = here - d
        if nx1 <= f and not visited[nx1]:
            visited[nx1] = True
            q.append((nx1, dist + 1))

        if nx2 >= 1 and not visited[nx2]:
            visited[nx2] = True
            q.append((nx2, dist + 1))

    if ans == int(1e9):
        print("use the stairs")
    else:
        print(ans)


f, s, g, u, d = map(int, input.readline().split())
visited = [False] * (f + 1)
bfs(s, g, f, u, d)
```



## BOJ_9205_맥주마시면서걸어가기

- 틀렸던코드

```python
'''
2020-12-09 19:55-(20:08밥-20:35컴백)-
출발 상근이네 -> 맥주한박스들고 출발(20개) 50미터에 한병씩 마심
맥주를 더 구매해야할 수 도 있음
편의점을 들렸을때 빈병은 버리고 새 맥주 병 살 수 있다(20개까지)
상근이와 친구들 행복하게 페스티벌 도착해야됨

송도는 직사각형 모양으로 생긴 도시
두 좌표 사이의 거리는 (x좌표 차이 + y좌표의 차)
행복하게 갈수있으면 happy, 아니면 sad출력

너무 오래 걸렸다...ㅠ
어려운 문제는 아닌데 설계를 잘못함
1. start는 home!
2. festival의 위치도 기록한 뒤, 편의점과 festival을 같은 infolist에 묶어서 home과의 거리가 짧은 순으로 정렬!
# 여기서 2번이 문제였다...home과의 거리란,,, festival과 반대로 멀어질수도있다는걸 생각못함ㅠㅠ->플로이드 와샬..알고리즘..공부하자ㅠ
3. info를 돌면서 festival에 도착하면 happy아니면 sad(거리비교 beer-dist/50>=0)

# 다시생각
집 -편의점 - Festival
이렇게 위치해있고 집-편의점 : a // 편의점 -Festival :b // 집-festival :c라면
a랑 b는 c보다 작아야된다! 그래야 집- 편의점-축제 순서가 됨!
c가 바로갈수있는 거리가 아니고 a는 갈수있다면 a,b가 c보다 작다면 편의점으로 내 위치 갱신
아니라면 다음 편의점과 반복
이렇게...해서 찾아보자....!
'''
import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    # 편의점 개수
    n = int(input())
    # 상근이네 집, 편의점,락페스티벌 좌표x,y
    home = list(map(int,input().split()))
    info = [list(map(int,input().split())) for _ in range(n)]
    festival = list(map(int,input().split()))
    # 거리순으로 일단 정렬은 했는데 만약에 c보다 b가 크다면 지나가게하자
    info.sort(key = lambda x:(abs(x[0]-home[0])+abs(x[1]-home[1])))
    # print(info)
    # print(festival)
    beer = 20
    sx,sy = home
    ex,ey = festival
    flag = False
    c = abs(sx-ex) + abs(sy-ey)
    if beer - c/50 >= 0:
        print('happy')
        flag = True
        continue
    for i in info:
        nx,ny = i
        a = abs(sx-nx) + abs(sy-ny)
        b = abs(nx-ex) + abs(ny-ey)
        c = abs(sx-ex) + abs(sy-ey)
        # 갈수 있다면
        if c <= 1000:
            print('happy')
            flag = True
            break
        # 편의점이 출발점과 끝점 사이에 있다면 시작점 갱신
        if a <= 1000 and a < c and b < c:
            sx,sy = nx,ny
        if a<=1000 and b <= 1000:
            print('happy')
            flag = True
            break
    if flag:
        continue
    if c <=1000 or b <=1000:
        print('happy')
    else:
        print('sad')

```

- 다시품

```python
import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

def BFS(start):
    global flag
    visited = set()
    q = deque()
    q.append(start)
    ex,ey = festival
    while q:
        px,py = q.popleft()
        if abs(px-ex) + abs(py-ey) <= 1000:
            flag = True
            return
        next_store = []
        for idx in range(N):
            nx,ny = store[idx]
            if abs(px-nx) + abs(py-ny) <= 1000 and (idx not in visited):
                visited.add(idx)
                next_store.append([nx,ny])
        q.extend(next_store)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    home = list(map(int,input().split()))
    store = [list(map(int,input().split())) for _ in range(N)]
    festival = list(map(int,input().split()))
    flag = False
    BFS(home)
    if flag:
        print('happy')
    else:
        print('sad')
```



- 승범코드

```python
def d():
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j: continue
            if abs(s[i][0] - s[j][0]) + abs(s[i][1] - s[j][1]) <= 1000:
                s_[i][j] = 1
                s_[j][i] = 1
def dfs(start):
    visit[start] = 1
    for i in range(n + 2):
        if s_[start][i] == 1 and visit[i] == 0:
            dfs(i)
t = int(input())
for i in range(t):
    n = int(input())
    s = [list(map(int, input().split())) for i in range(n + 2)]
    s_ = [[0] * (n + 2) for i in range(n + 2)]
    visit = [0 for i in range(n + 2)]
    d()
    dfs(0)
    if visit[n + 1] == 1: print("happy")
    else: print("sad")
```

- 다른사람코드

```python
import sys
input = sys.stdin.readline

def bfs(arr, n):
    visited = {0: True} #dict 형태
    queue = [0]
    while queue:
        tmp = []
        pos = queue.pop(0)
        if pos == n - 1:
            return 'happy'
        for i, (x, y) in enumerate(arr): #좌표 enumerate
            if i in visited:
                continue
            distance = abs(arr[pos][0] - x) + abs(arr[pos][1] - y)
            if distance <= 1000: #맥주 20병 -> 1000으로 제한 
                tmp.append(i)
                visited[i] = True
        queue.extend(tmp)
    return 'sad'


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for _ in range(n + 2):
            x,y = map(int,input().split())
            arr.append((x,y))
        print(bfs(arr, n + 2))
```

```python
import sys
input = sys.stdin.readline
from _collections import deque


def BFS(start, end, mart_list):
    q = deque([(start)])
    visited = {(start)}    # 사실 이것도 필요 없네. 코드를 간다하게 만들기 위해 넣자.
    while q:
        pos = q.popleft()
        if abs(pos[0] - end[0]) + abs(pos[1] - end[1]) <= 1000:
            return "happy"

        new_append = []
        for mart in mart_list:
            if not mart in visited:
                if abs(pos[0] - mart[0]) + abs(pos[1] - mart[1]) > 1000 :
                    continue
                visited.add(mart)
                q.append(mart)
                new_append.append(mart)

        for mart in new_append:
            mart_list.remove(mart)

    return "sad"

result = []
for _ in range(int(input())):
    n_mart = int(input())
    start = tuple(map(int, input().split()))
    mart_list = []
    for _ in range(n_mart):
        mart_list.append(tuple(map(int, input().split())))
    end = tuple(map(int, input().split()))
    result.append(BFS(start, end, mart_list))

for x in result:
    print(x)
```

```python
import sys
I = sys.stdin.readline
def dfs(nowR, nowC):
    global happyFlag
    if happyFlag:
        return
    if abs(nowR -rock[0]) + abs(nowC-rock[1]) <= 1000:
        happyFlag = True
        return
    for d in range(0,de):
        if abs(nowR + - deList[d][0])+ abs(nowC -deList[d][1]) <= 1000 and not visit[d]:
            visit[d] = True
            dfs(deList[d][0], deList[d][1])


test = int(I())
for t in range(0,test):
    de = int(I())
    home = list(map(int,I().split()))
    deList = []
    for d in range(0,de):
        deList.append(list(map(int,I().split())))
    rock = list(map(int,I().split()))

    visit = [False] * de
    happyFlag = False

    dfs(home[0], home[1])

    if happyFlag:
        print('happy')
    else:
        print('sad')
```



## BOJ_2573_빙산

> pypy로 품 import해놓은것 떄문에 메모리 초과가 났다 앞으로 제출할때 필요없는거 다 지워주자

```python
'''
2020-12-10 11-
빙산이 주어짐, 0과 접한 개수만큼 빙산이 다 녹음 두덩어리 이상으로 분리되지 않으면 0출력
분리된다면 최소 시간 구하기

1. 빙산에 4방향으로 보면서 0개수만큼 빼고 temp배열에 담아주기
2. 모두 봤다면 temp를 보면서 덩어리가 나뉘어졌는지 확인
3. 다시 반복

BFS,DFS는 시간초과, 메모리초과가 난다...
시간초과를 어떻게 줄이지ㅠ
#배열을 만들어서 하지말고 [i,j,zero]를 담아줘서 전부 확인 후에 arr에 직접 i,j -zero해보자
'''
import sys
input = sys.stdin.readline
from collections import deque

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def DFS(i,j):
    visited.add((i,j))
    zero = 0
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        if (ni,nj) in visited:
            continue
        if not arr[ni][nj]:
            zero+=1
            continue
        DFS(ni,nj)
    change.append([i,j,zero])


def BFS(i,j):
    q = deque()
    q.append([i,j])
    visited.add((i,j))
    while q:
        pi,pj = q.popleft()
        zero = 0
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if (ni,nj) in visited:
                continue
            if not arr[ni][nj]:
                zero+=1
                continue
            visited.add((ni,nj))
            q.append([ni,nj])
        change.append([pi,pj,zero])

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
year = 0
change = deque()
while True:
    cnt = 0
    # temp = [[0 for j in range(M)] for i in range(N)]
    visited = set()
    # 처음, 마지막은 0이니까 안봐도됨
    for i in range(1,N-1):
        for j in range(1,M-1):
            if arr[i][j] and ((i,j) not in visited) and cnt<2:
                cnt +=1
                # DFS(i,j)
                BFS(i,j)
    # print(change)
    if cnt >=2:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    year += 1
    while change:
        i,j,zero = change.popleft()
        arr[i][j] -= zero
        if arr[i][j] <0:
            arr[i][j] = 0
    # for x in arr:
    #     print(x)
```

- 다른 코드 보고 ice만 따로 담아주고 갱신해주니까 시간초과안남!!!!!

```python
import sys
input = sys.stdin.readline
from collections import deque

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def BFS(i,j):
    q = deque()
    q.append([i,j])
    visited.add((i,j))
    while q:
        pi,pj = q.popleft()
        zero = 0
        for d in range(4):
            ni = pi + di[d]
            nj = pj + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if (ni,nj) in visited:
                continue
            if not arr[ni][nj]:
                zero+=1
                continue
            visited.add((ni,nj))
            q.append([ni,nj])
        change.append([pi,pj,zero])

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
year = 0
change = deque()
ice = deque()
for i in range(1,N-1):
    for j in range(1,M-1):
        if arr[i][j]:
            ice.append((i,j))
while True:
    cnt = 0
    # temp = [[0 for j in range(M)] for i in range(N)]
    visited = set()
    while ice:
        i = ice.popleft()
        if i not in visited:
            cnt += 1
            BFS(i[0],i[1])
    if cnt >=2:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    year += 1
    ice =deque()
    while change:
        i,j,zero = change.popleft()
        arr[i][j] -= zero
        if arr[i][j] <=0:
            arr[i][j] = 0
        else:
            ice.append((i,j))
    # for x in arr:
    #     print(x)
```



- 다른코드

```python
import sys
from collections import deque


def bfs():
    attached = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque([ice[0]])
    visited[ice[0][0]][ice[0][1]] = True
    while q:
        x, y = q.popleft()
        zero_count = 0
        attached += 1
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 0:
                zero_count += 1
                continue
            if board[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))

        if board[x][y] - zero_count != 0:
            board[x][y] -= zero_count
        else:
            board[x][y] = -1

    return attached


N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ice = []
for i in range(N):
    for j in range(M):
        if board[i][j]:
            ice.append((i, j))

c = 0
while True:
    new_ice = []
    if len(ice) == 0:
        c = 0
        break
    a = bfs()
    if len(ice) != a:
        break
    for (x, y) in ice:
        if board[x][y] < 0:
            board[x][y] = 0
        else:
            new_ice.append((x, y))

    ice = new_ice[:]
    c += 1

print(c)

```

```python
import sys

class IceBerg:

    piece = int()
    icePosition = []

    def __init__(self, n, m, ice):
        self.n = n
        self.m = m
        self.ice = ice

        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if self.ice[i][j] > 0:
                    self.icePosition.append([i, j])

    def icebergCount(self):
        ret = 0
        visit = [[False] * m for _ in range(n)]
        for i, j in self.icePosition:
            if visit[i][j] is False:
                ret += 1
                self.bfs(visit, i, j)

        self.piece = ret
        return ret

    def bfs(self, visit, y, x):
        qu = [[y, x]]
        visit[y][x] = True

        while len(qu):
            posy, posx = qu.pop()

            if self.ice[posy][posx - 1] > 0 and visit[posy][posx - 1] is False:
                visit[posy][posx - 1] = True
                qu.append([posy, posx - 1])
            if self.ice[posy][posx + 1] > 0 and visit[posy][posx + 1] is False:
                visit[posy][posx + 1] = True
                qu.append([posy, posx + 1])
            if self.ice[posy - 1][posx] > 0 and visit[posy - 1][posx] is False:
                visit[posy - 1][posx] = True
                qu.append([posy - 1, posx])
            if self.ice[posy + 1][posx] > 0 and visit[posy + 1][posx] is False:
                visit[posy + 1][posx] = True
                qu.append([posy + 1, posx])

    def melting(self):
        melt = []
        tmpPosition = []

        for i, j in self.icePosition:
            cnt = 0
            if self.ice[i][j - 1] == 0:
                cnt += 1
            if self.ice[i][j + 1] == 0:
                cnt += 1
            if self.ice[i - 1][j] == 0:
                cnt += 1
            if self.ice[i + 1][j] == 0:
                cnt += 1

            if cnt > 0:
                melt.append([i, j, cnt])
            else:
                tmpPosition.append([i, j])

        for i, j, cnt in melt:
            self.ice[i][j] -= cnt
            if self.ice[i][j] < 0:
                self.ice[i][j] = 0
            if self.ice[i][j] != 0:
                tmpPosition.append([i, j])

        self.icePosition = tmpPosition

n, m = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

iceberg = IceBerg(n, m, ice)
ans = 0

while iceberg.icebergCount() == 1:
    ans += 1
    iceberg.melting()

if iceberg.piece >= 2:
    print(ans)
else:
    print(0)

```



## BOJ_2583_영역구하기

> [BOJ_2583_영역구하기](https://www.acmicpc.net/problem/2583)

```python
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
```

- 다른코드

```python
import sys
M,N,K = map(int, sys.stdin.readline().split())
g = [[0]*M for _ in range(N)]
for _ in range(K):
    frmx, frmy, tox, toy = map(int, sys.stdin.readline().split())

    for x in range(frmx, tox):
        for y in range(frmy, toy):
            g[x][y] = 1

land = []

def dfs(x,y):
    count = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    g[x][y] = 1
    stack = [(x,y)]

    while stack:
        x,y = stack.pop()
        for i in range(4):
            nxtx = x+dx[i]
            nxty = y+dy[i]

            if 0<=nxtx<N and 0<=nxty<M and g[nxtx][nxty] == 0:
                g[nxtx][nxty] = 1
                stack.append((nxtx, nxty))
                count += 1

    land.append(count)

for i in range(N):
    for j in range(M):
        if g[i][j] == 0:
            dfs(i,j)

land.sort()
print(len(land))
print(" ".join(str(x) for x in land))
```

```python
def adj(i, j, m, n, f):
    if i and f[i-1][j]:
        yield (i-1, j)
    if j and f[i][j-1]:
        yield (i, j-1)
    if i-m+1 and f[i+1][j]:
        yield (i+1, j)
    if j-n+1 and f[i][j+1]:
        yield (i, j+1)


def main1(inputs = None):
    m, n, k = map(int, input().split())
    area = [[1] * n for y in range(m)]
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for y in range(y1, y2):
            area[y][x1:x2] = [0] * (x2 - x1)

    h = 100
    res = []

    for y, row in enumerate(area):
        for x, num in enumerate(row):
            if num:
                area[y][x] = False
                que = [(y, x)]
                s = 1
                while que:
                    i0, j0 = que.pop(0)
                    for u, v in adj(i0, j0, m, n, area):
                        que.append((u, v))
                        area[u][v] = False
                        s += 1
                res.append(s)
    print(len(res))
    res.sort()
    print(' '.join([str(i) for i in res]))

main1()
```

## BOJ_1987_알파벳

> [BOJ_1987_알파벳](https://www.acmicpc.net/problem/1987)
>
> DFS로 풀면 시간초과..BFS로 풀면 통과했따..
>
> set을 이용하니 Python3에서도 통과

```python
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

```

- python3으로 통과한 코드

```python
import sys
from collections import deque


# https://www.acmicpc.net/problem/1987
#
# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는
# 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

# Input Example
# 2 4
# CAAB
# ADCB


def dfs(x, y):
    global board, R, C

    max_depth = 0

    queue = set()
    queue.add((x, y, board[y][x]))

    while queue:
        current_x, current_y, current_visited = queue.pop()
        max_depth = max(max_depth, len(current_visited))
        if max_depth == 26:
            return 26

        for movement in movement_array:
            next_x = current_x + movement[0]
            next_y = current_y + movement[1]
            if 0 <= next_x < C and 0 <= next_y < R and board[next_y][next_x] not in current_visited:
                queue.add((next_x, next_y, current_visited + board[next_y][next_x]))

    return max_depth


R, C = map(int, sys.stdin.readline().split())
board = []
for _ in range(R):
    row = list(sys.stdin.readline().strip())
    board.append(row)

movement_array = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]
start = (0, 0)
print(dfs(*start))

```



## BOJ_10026_적록색약

> [BOJ_10026_적록색약](https://www.acmicpc.net/problem/10026)

```python
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

di = [0,1,0,-1]#우하좌상
dj = [1,0,-1,0]
def DFS(i,j,color,blindness):
    global normal, blindCnt
    visited[i][j] = True
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if visited[ni][nj]:
            continue
        if color != arr[ni][nj]:
            # 적록색약인 경우
            if blindness and (color in colorList and arr[ni][nj] in colorList):
                DFS(ni,nj,arr[ni][nj],blindness)
            else:
                continue
        DFS(ni, nj, arr[ni][nj], blindness)


N = int(input())
arr = [list(input()) for _ in range(N)]

visited = [[False for j in range(N)] for i in range(N)]
colorList = ['R','G']
normal = 0
blindCnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            # 적록색약인경우
            blindCnt += 1
            DFS(i,j,arr[i][j],True)
visited = [[False for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            # 아닌경우
            normal += 1
            DFS(i,j,arr[i][j],False)
print(normal,blindCnt)
```

- 배열을 다르게 받았다

```python
'''
적록색약 빨간색, 초록색 차이를 거의 느끼지 못함
R(빨강), G(초록), B(파랑)
상하좌우로 같은색상이 인접해 있으면 같은 구역에 속함(색상의 차이를 느끼지 못하는 경우 같은 영역이라 함)
1. 배열을 입력 받는다.
2. DFS로 보고, 적록색약이 아닌경우, 색이 다를 떄 cnt를 +1해줌
3. 적록색약인 경우, 빨간색이나 초록색일때 다음 색이 빨간색이나 초록색이면 두 색을 같은 색으로 판단한다.
적록색약은 배열을 받을 때 G를 R로 바꿔줌
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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
```



- 다른코드

```python
#백준 10026번 - 적록색약

'''

문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1)
하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와
아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

예제 출력 1
4 3
'''


import sys

sys.setrecursionlimit(1000000)
a = int(sys.stdin.readline())
graphForNomal= [([0] * a) for _ in range(a)]
graphForRedGreen= [([0] * a) for _ in range(a)]
count_Nomal = 0
count_Red_Green = 0

for i in range(a) :
    str = sys.stdin.readline()
    for j in range(a) :
        graphForNomal[i][j] = str[j]
        if str[j] == "R" :
            graphForRedGreen[i][j] = "G"
        else :
            graphForRedGreen[i][j] = str[j]

def nomal_Dfs(graph, color, sero, garo) :
    if garo + 1 < a and (color == graph[sero][garo + 1]):
        graph[sero][garo + 1] = "A"
        nomal_Dfs(graph, color, sero, garo + 1)

    if sero + 1 < a and (color == graph[sero + 1][garo]) :
        graph[sero + 1][garo] = "A"
        nomal_Dfs(graph, color, sero + 1, garo)

    if garo - 1 > -1 and (color == graph[sero][garo - 1]) :
        graph[sero][garo - 1] = "A"
        nomal_Dfs(graph, color, sero, garo - 1)

    if sero - 1 > -1 and (color == graph[sero - 1][garo]) :
        graph[sero - 1][garo] = "A"
        nomal_Dfs(graph, color, sero - 1, garo)

#이거 필요 없을듯..?
'''
def red_Green_Dfs(color, sero, garo) :
    if garo + 1 < a and ()
'''

for i in range(a) :
    for j in range(a) :
        if graphForNomal[i][j] != "A" :
            temp = graphForNomal[i][j]
            graphForNomal[i][j] = "A"
            count_Nomal = count_Nomal + 1
            nomal_Dfs(graphForNomal, temp, i, j)

for i in range(a) :
    for j in range(a) :
        if graphForRedGreen[i][j] != "A" :
            temp = graphForRedGreen[i][j]
            graphForRedGreen[i][j] = "A"
            count_Red_Green = count_Red_Green + 1
            nomal_Dfs(graphForRedGreen, temp, i, j)

print(count_Nomal, end = ' ')
print(count_Red_Green)
```



## BOJ_1941_소문난칠공주

> [BOJ_1941_소문난칠공주](https://www.acmicpc.net/problem/status/1941/28/1)

```python
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
```

- 다른코드

```python
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
princess = deque()
ans = set()
A = [[] for _ in range(5)]
visit = [[False] * 5 for _ in range(5)]

def go(n, cnt):
    if (cnt + (7 - n) < 4):
        return

    if n == 7:
        if cnt >= 4:
            temp = list(princess)
            temp.sort()
            temp = tuple(temp)
            ans.add(temp)
        return

    possible = set()
    for node in princess:
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx < 0 or ny < 0 or nx == 5 or ny == 5 or visit[nx][ny]:
                continue

            possible.add((nx,ny))

    for node in possible:

        visit[node[0]][node[1]] = True
        princess.append(node)
        if A[node[0]][node[1]] == 'S':
            go(n+1, cnt+1)
        else:
            go(n+1, cnt)
        princess.pop();
        visit[node[0]][node[1]] = False

for i in range(5):
    A[i] = list(input().rstrip())

for i in range(5):
    for j in range(5):
        if A[i][j] == 'S':
            visit[i][j] = True
            princess.append((i,j))
            go(1,1)
            princess.popleft()

print(len(ans))
```



## 프로그래머스_타겟넘버

> [프로그래머스_타겟넘버](https://programmers.co.kr/learn/courses/30/lessons/43165)

```python
def solution(numbers, target):
    answer = 0

    def dfs(L,s) : 
        nonlocal answer
        if L == len(numbers) : 
            if s == target : 
                answer += 1
        else : 
            dfs(L+1,s+numbers[L])
            dfs(L+1,s-numbers[L])

    dfs(0,0)
    return answer
```

- 다른풀이

```python
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
```

```python
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
```

## 프로그래머스_네트워크

> [프로그래머스_네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)

```python
def solution(n, computers):
    answer = 0

    def DFS(pi,pj):
        visited[pi][pj] = True
        for next in range(n):
            if visited[pj][next]:
                continue
            if not computers[pj][next]:
                continue
            DFS(pj,next)


    visited = [[False for j in range(n)] for i  in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and computers[i][j]:
                DFS(i,j)
                answer += 1

    return answer
```

- 다른 풀이

```python
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer
```

```python
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))
```

## 프로그래머스_단어변환

```python
'''
begin이 target으로 변환돼야되는데 한번에 한개의 알파벳만 바꿀수 있고 그 단어가 words에 있는 단어야 된다.
1. begin과 target이 다른 것을 words에 있는 단어 중 begin과 같은 단어가 1개 차이나고 target과 begin이랑 공통되는 것이 1개 더 많아야된다.
2. 바뀐 것으로는 다시 바뀌지 않게 words에서 뺴줌
'''


def solution(begin, target, words):
    answer = 0
    bigin_target_cnt = 0
    for i in range(len(begin)):
        if begin[i] == target[i]:
            bigin_target_cnt += 1
    print('begin과 target공통', bigin_target_cnt)
    while True:
        if begin == target:
            break
        change_target = [0, 0]
        for i in range(len(words)):
            word = words[i]
            begin_cnt = 0
            target_cnt = 0
            for w in range(len(word)):
                if word[w] == begin[w]:
                    begin_cnt += 1
                if word[w] == target[w]:
                    target_cnt += 1
            if (begin_cnt == len(begin) - 1) and (change_target[1] < target_cnt):
                change_target = [i, target_cnt]
        if change_target != [0, 0]:
            print(begin, '->', words[change_target[0]])
            begin = words[change_target[0]]
            words.pop(change_target[0])
            bigin_target_cnt += 1
            answer += 1
        else:
            answer = 0
            break

    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))
```

- 다른풀이

```python
def solution(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target:
                    return answer
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1:
                    temp_Q.append(words.pop(i))

        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1

```

```python
from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)

```

## 프로그래머스_여행경로

> 이렇게 풀었는데 틀렸당,,,다시 풀어봐야지

```python
'''
1. tickets가 주어지고, [출발,도착]으로 진행됨
2. DFS를 돌려가며 방문처리, 모두 봄고 전체 방문 처리되면 answer에 넣은 것중 알파벳순서 빠른거로 바꿈
'''
def solution(tickets):
    result = [""] * (len(tickets)+1)
    def DFS(idx):
        start, end = tickets[idx]
        for t in range(len(tickets)):
            ticket_start, ticket_end = tickets[t]
            if visited[t]:
                continue
            if ticket_start != end:
                continue
            visited[t] = visited[idx] + 1
            DFS(t)
        return

    for i in range(len(tickets)):
        visited = [0 for _ in range(len(tickets))]
        answer = [""] * (len(tickets))
        visited[i] = 1
        DFS(i)
        for v in range(1,len(tickets)+1):
            if answer[v-1]:
                break
            if v not in visited:
                break
            idx = visited.index(v)
            answer[v-1] = tickets[idx]
        else:
            if result[0] != "":
                print(visited)
                for x in answer:
                    print(x)
                temp = [""]*len(result)
                temp[0] = answer[0][0]
                for a in range(1, len(tickets)):
                    temp[a] = answer[a][0]
                temp[len(tickets)] = answer[-1][1]

                for t in range(len(result)):
                    word = temp[t]
                    for w in range(len(result[t])):
                        if ord(result[t][w]) < ord(word[w]):
                            break
                    else:
                        result = temp

            else:
                print(visited)
                for x in answer:
                    print(x)
                result[0] = answer[0][0]
                for a in range(1, len(tickets)):
                    result[a] = answer[a][0]
                result[len(tickets)] = answer[-1][1]
                print(result)


    return result

print(solution( [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
```

- 다른 풀이

```python
def solution(tickets):
    connections, visited = {}, {}

    for tic in tickets:
        connections[tic[0]] = list()
        visited[tic[0]+tic[1]]=0

    num_airport=0

    for tic in tickets:
        visited[tic[0] + tic[1]] +=1
        num_airport+=1

        connections[tic[0]].append(tic[1])
        connections[tic[0]].sort()

    result_set = list()


    for next_port in connections['ICN']:
        tmp=visited.copy()
        tmp['ICN'+next_port]-=1
        dfs(next_port, 1, num_airport, result_set, tmp,
            ['ICN', next_port], connections)

    result_set.sort()

    return result_set[0]


def dfs(v, count, num, result_set, visited, line, connections):

    if count == num:

        result_set.append(line)
        return

    if not v in connections:
        return


    for next_port in connections[v]:
        if  visited[v + next_port]!=0:

            visited[v + next_port] -=1
            tmp = line[:]
            tmp.append(next_port)
            dfs(next_port, count + 1, num, result_set, visited, tmp,
                connections)
            visited[v+next_port]+=1


# solution(
# [["ICN","BOO" ], [ "ICN", "COO" ], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]])
```



## BOJ_1697_숨바꼭질

> [BOJ_1697_숨바꼭질](https://www.acmicpc.net/problem/1697)
>
> - 이전 풀이 정답
>
> ```python
> from collections import deque
> def BFS(n):
>     q = deque()
>     q.append(n)
>     while q:
>         X = q.popleft()
>         if X == K:
>             return dist[K]
>         a = X-1
>         b = X+1
>         c = X*2
>         if 0 <= a < MAX and dist[a] ==0:
>             dist[a] = dist[X]+1
>             q.append(a)
>         if 0 <= b < MAX and dist[b] ==0:
>             dist[b] = dist[X]+1
>             q.append(b)
>         if 0 <= c <MAX and dist[c] ==0:
>             dist[c] = dist[X]+1
>             q.append(c)
> 
> N,K = map(int,input().split())
> # N,K=5,17
> MAX = 100001
> dist = [0 for _ in range(MAX)]
> print(BFS(N))
> ```
>
> 

```python
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
```

- 다른풀이

```python
def c(n,k):
    if n>=k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return 1+min(c(n,k-1),c(n,k+1))
    else:
        return min(k-n, 1+c(n,k//2))
    
n, k = map(int,input().split())
print(c(n,k))
```



```python
import sys
input = sys.stdin.readline

s, e = map(int, input().split())

def sol(s, e):

    if s >= e:
        return s-e
 
    answer = e-s
    step = 0
    nums = [e]

    while nums:
        step += 1
        temp = []
        for n in nums:
            if n%2:
                if n-1 == s:
                    answer = min(answer, step)
                else:
                    temp.append(n-1)
                    temp.append(n+1)
            else:
                if n//2 < s:
                    s - n//2 + step
                    answer = min(answer, s - n//2 + step, n - s + step - 1)
                elif n//2 == s:
                    answer = min(answer, step)
                else:
                    temp.append(n//2)
        nums = temp

    return answer

print(sol(s, e))
```



## BOJ_12851_숨바꼭질2

> [BOJ_12851_숨바꼭질2](https://www.acmicpc.net/problem/1697)

```python
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
            # 지금 next에 있는 값(dist[next])이 갱신할 값(dist[p]+1)보다 작다면 지나가야됨!
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
```

- 다른코드보고 다시 푼 코드

```python
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

```



- 다른코드

```python
from collections import deque

N, K = map(int, input().split())

# N이 K보다 크면 -1로 내려갈수밖에 없어서 N-K초
if N >= K:
    print(N-K)
    print(1)

else:
    visited = [False] * 100001
    ans = 100001 #최소 초 초기값
    amount = 0 #최소 초 경우의수
    q = deque()
    q.append((K, 0)) #현위치, 현위치 초수
    while q:
        pos, cnt = q.popleft()
        visited[pos] = True #현위치 방문표시
		
        # 현 위치보다 초수 넘어가면 건너뜀
        if cnt > ans:
            continue
		
        # 위치가 N에 도달하면
        if pos == N:
            # cnt가 ans(최소초수)보다 작으면 갱신, amount도 1개로 리셋
            if cnt < ans:
                ans = cnt
                amount = 1
            elif cnt == ans: #최소초수랑 같다면 경우의수 1증가
                amount += 1
        
        else:
            # 짝수일때 방문도 안했다면 q에 pos//2 추가
            if not pos % 2 and not visited[pos % 2]:
                q.append((pos // 2, cnt + 1))
            # 1뺀게 범위에서 벗어나지 않고 방문 안했다면 q에 pos-1추가
            if 0 <= pos - 1 and not visited[pos-1]:
                q.append((pos - 1, cnt + 1))
            # 1더한게 범위에서 벗어나지 않고 방문 안했다면 q에 pos+1추가
            if pos + 1 <= 100000 and not visited[pos+1]:
                q.append((pos + 1, cnt + 1))

    print(ans)
    print(amount)
```

```python
import sys
from collections import deque

MAX_POINT = 100001

def bfs():
  global cnt,min_time,MAX_POINT

  q = deque()
  q.append((K,0))
  visited[K] = True

  while q:
    n,d = q.popleft()

    visited[n] = True

    if n == N:
      min_time = d
      cnt += 1
      break
      
    if n%2==0:
      if 0<=n//2<MAX_POINT:
        if not visited[n//2]:
          q.append((n//2,d+1))

    if 0<=n-1<MAX_POINT:
      if not visited[n-1]:
        q.append((n-1,d+1))
        
    if 0<=n+1<MAX_POINT:
      if not visited[n+1]:
        q.append((n+1,d+1))
        
  while q:
    n,d = q.popleft()
    
    if n == N and d==min_time:
      cnt+= 1
    
N,K = map(int,sys.stdin.readline().split())

visited = [False]*(MAX_POINT)
min_time = 0
cnt = 0

bfs()

print(min_time)
print(cnt)
```



##  프로그래머스_49189_가장 먼노드

> [프로그래머스_49189_가장 먼노드](https://programmers.co.kr/learn/courses/30/lessons/49189)

```python
from collections import deque

def solution(n, edge):
    answer = 0
    adj = [[] * (n+1) for i in range(n+1)]
    for i in range(len(edge)):
        s,e = edge[i]
        adj[s].append(e)
        adj[e].append(s)
    dist = [0] * (n+1)
    q = deque(adj[1])
    dist[1] = 1
    for i in q:
        dist[i] = dist[1] + 1
    while q:
        now = q.popleft()
        for i in adj[now]:
            next = i
            if dist[next]:
                continue
            dist[next] = dist[now] + 1
            q.append(next)
    MAX = max(dist)
    for i in dist:
        if i == MAX:
            answer += 1
    return answer
```

- 다른 풀이

```python
def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer
```

```python
class Graph():
    def __init__(self, num_edge, vertices):
        self.vertex = [None]
        self.num_edge = num_edge
        for num in range(num_edge):
            self.vertex.append([])
        self.createGraph(vertices)
    def createGraph(self, vertices):
        for vertex in vertices:
            self.vertex[vertex[0]].append(vertex[1])
            self.vertex[vertex[1]].append(vertex[0])
    def shortestNodes(self):
        dist = [float('inf')] * (self.num_edge + 1)
        q = [(1, 0)]
        while len(q) > 0:
            (cur, depth) = q.pop(0)
            if depth < dist[cur]:
                dist[cur] = depth
                for edge in self.vertex[cur]:
                    q.append((edge, depth + 1))
        dist = [x for x in dist if x < float('inf')]
        print(dist)
        max_dist = max(dist)
        dist = list(filter(lambda x: x == max_dist, dist))
        return len(dist)

def solution(n, edge):
    g = Graph(n, edge)
    return g.shortestNodes()

```



