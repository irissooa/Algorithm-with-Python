def solution(numbers, target):
    temp = set()
    LEN = len(numbers)
    q = [[numbers[0]],[-numbers[0]]]
    di = [1,-1]
    while q:
        now = q.pop(0)
        N = len(now)
        if N == LEN:
            if sum(now) == target:
                temp.add(tuple(now))
        else:
            for d in range(2):
                res = numbers[N]*di[d]
                next = now[:] + [res]
                q.append(next)
    return len(temp)

print(solution([1, 1, 1],3))