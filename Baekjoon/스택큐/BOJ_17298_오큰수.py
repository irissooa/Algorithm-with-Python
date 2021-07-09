'''
크기가 N인 수열
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수
그러한 수가 없으면 -1
[3,5,2,7] : NGE(1) = 5, NGE(2) = 7 NGE(3) = 7, NGE(4) = -1
1. (0,N-1)으로 보는데 현재 것이 다음 수 보다 작다면 result에 다음 수 담기
2. 만약 다음수가 작다면 그 다음수를 비교
'''
import sys
input = sys.stdin.readline

'''
# 시간초과
sys.setrecursionlimit(10**6)

def check(idx,num):
    if idx == N:
        return -1
    if arr[idx] > num:
        return arr[idx]
    else:
        return check(idx+1,num)

N = int(input())
arr = list(map(int,input().split()))
result = [0] * (N-1)+[-1]

for i in range(N-1):
    if arr[i+1] > arr[i]:
        result[i] = arr[i+1]
    else:
        result[i] = check(i+1,arr[i])
print(" ".join(map(str,result)))

# 시간초과
def check(li):
    res = []
    for i in range(len(li)-1):
        idx = i
        while idx < N-1:
            if li[i] >= li[idx+1]:
                idx += 1
            else:
                res.append(li[idx+1])
                break
        if idx == N-1:
            res.append(-1)
    res.append(-1)
    return res

N = int(input())
arr = list(map(int,input().split()))
res = check(arr)
print(' '.join(str(x) for x in res))
'''
def check(li):
    res = [0]*len(li)
    stack = []
    for i in range(len(li)-1,-1,-1):
        while stack and stack[-1] <= li[i]:
            stack.pop()
        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]
        stack.append(li[i])
    return res

N = int(input())
arr = list(map(int,input().split()))
res = check(arr)
print(' '.join(map(str,res)))