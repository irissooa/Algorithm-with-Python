'''
두 소수의 합으로 나타내는 골드바흐 파티션을 구하라
만약 값이 여러개면 차이가 적은 것으로 출력
1. 수를 입력받고
2. N보다 작은 소수들을 리스트에 담고
3. 그 리스트를 더하면서 N이 되는 값을 결과에 담고 그 차가 적은 것을 출력
'''
import sys
input = sys.stdin.readline

# def decimal(n):
#     decimalList = []
#     for d in range(2,n):
#         for i in range(2,d):
#             if d % i == 0:
#                 break
#         else:
#             decimalList.append(d)
#     result = []
#     LEN = len(decimalList)
#     for d1 in range(LEN):
#         for d2 in range(d1,LEN):
#             if decimalList[d1] + decimalList[d2] > N:
#                 break
#             elif decimalList[d1] + decimalList[d2] == N:
#                 result.append((decimalList[d1],decimalList[d2]))
#     ans = []
#     if len(result) >= 2:
#         MIN = 987654321
#         while result:
#             r1,r2 = result.pop(0)
#             if MIN > abs(r1-r2):
#                 MIN = abs(r1-r2)
#                 ans = [r1,r2]
#     else:
#         r1,r2 = result.pop()
#         ans = [r1,r2]
#     return ans
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     ans = decimal(N)
#     print(*ans)

# 에라토스테네스의 체
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False
    return sieve


def gold(primes, n):
    index = 0
    while True:
        if primes[n // 2 - index] and primes[n // 2 + index]:
            return (n // 2 - index, n // 2 + index)
        index += 1


primes = prime_list(10001)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    answer = gold(primes, N)
    print(answer[0], answer[1])