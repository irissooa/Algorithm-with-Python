'''
논문 n편중 h번 이상 인용된 논문이 h편 이상
나머지 논문이 h번 이하 인용됐다면 h의 최대값이 이 과학자의 H-Index
citations 어떤 과학자가 발표한 논문의 인용횟수를 담은 배열

1. citations 정렬, h는 citations 처음부터 확인
2. 가장 많이 포함하는 최댓값 구하기
* h는 ciatations에 없는 수여도 된다
'''


# def solution(citations):
#     answer = 0
#     citations.sort(reverse=True)
#     n = len(citations)
#     h = citations[0]
#     while h >= 0:
#         high,low = 0,0
#         for c in range(n):
#             if h <= citations[c]:
#                 high += 1
#             else:
#                 low = n-c
#                 break
#         if h > answer and h <= high and h >= low:
#             answer = h
#         h -= 1
#     return answer

# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min,enumerate(citations,start=1)))
#     return answer

def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
    return 0

print(solution([3, 0, 6, 1, 5]))