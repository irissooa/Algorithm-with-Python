'''
1. numbers를 list로 만들어서 수를 순열로 만듦
2.그 수가 소수인지 확인
'''


def solution(numbers):
    def isPrime(n):
        sieve = [True] * (n + 1)
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i]:
                for j in range(i * 2, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    def perm(chosen, used, cnt):
        nonlocal answer
        if len(chosen) == cnt:
            temp = ''.join(chosen)
            if int(temp) in prime_list and int(temp) not in answer:
                answer.append(int(temp))
            return
        for i in range(len(numbers)):
            if not used[i]:
                chosen.append(numbers[i])
                used[i] = 1
                perm(chosen, used,cnt)
                used[i] = 0
                chosen.pop()
    answer = []
    numbers = list(numbers)
    N = len(numbers)
    prime_list = isPrime(10**7)
    for c in range(1,N+1):
        used = [0 for _ in range(len(numbers))]
        perm([], used,c)

    return len(answer)

print(solution("17"))
print(solution("011"))