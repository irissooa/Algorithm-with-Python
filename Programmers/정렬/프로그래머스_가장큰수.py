'''
0또는 양의 정수, 이어붙여 만들 수 있는 가장 큰 수
numbers의 수를 재배치하여 이어붙여 가장 큰 수를 만들기
문자로 해서 앞의 수가 큰걸로 내림차순해서 정렬한 뒤, MAX로 설정 후, 자리바꿔 확인
순열로 자리 바꿔 MAX랑 비교
'''


def solution(numbers):
    answer = '0'

    def perm(a):
        i = len(a) - 1
        while i > 0 and a[i - 1] >= a[i]:
            i -= 1
        if i <= 0:
            return False
        j = len(a) - 1
        while a[j] <= a[i - 1]:
            j -= 1

        a[i - 1], a[j] = a[j], a[i - 1]

        j = len(a) - 1
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        return True
    idx = [x for x in range(len(numbers))]
    while True:
        temp = ''
        for i in idx:
            temp += str(numbers[i])
        if int(temp) > int(answer):
            answer = temp
        if not perm(idx):
            break
    return answer

print(solution([6, 10, 2]))
print(solution([3,30,34,5,9]))
