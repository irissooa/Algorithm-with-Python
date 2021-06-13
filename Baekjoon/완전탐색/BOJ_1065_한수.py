'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룸, 그 수를 한수
연속된 두개의 수의 차이가 일정한 수열
1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력
1. N만큼의 빈 배열을 만들어 해당 idx+1의 수까지의 한수 개수를 입력한다.
2. 해당 수의 한수 개수는 그전 idx의 수+ 해당 수가 한수인지 아닌지(0또는 1)을 더한값
'''
import sys
input = sys.stdin.readline

def check(num):
    if len(num) <= 2:
        nums[int(num)-1] = nums[int(num)-2] + 1
        return
    d = int(num[1]) - int(num[0]) # 공차
    for n in range(1, len(num)-1):
        if int(num[n]) + d != int(num[n+1]):
            nums[int(num)-1] = nums[int(num)-2]
            return
    nums[int(num)-1] = nums[int(num)-2] + 1
    return

N = int(input())
nums = [0] * N
nums[0] = 1
for i in range(1,N):
    check(str(i+1))
print(nums[N-1])