'''
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제
ACAYKP와 CAPCAK의 LCS는 ACAK가 된다
1. word1을 처음부터 word2의 단어 앞부터 일치하는 것을 담는다
2. 그렇게 담은 결과중 제일 긴 것을 갱신
'''
import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()
N1,N2 = len(word1),len(word2)
dp = [[0 for j in range(N2+1)] for i in range(N1+1)]

for s in range(N1):
    for n in range(N2):
        # 탐색 시 서로 같은 문자가 추가 된다면
        if word1[s] == word2[n]:
            # 같은 문자가 추가 되기 전 가장 긴 문자열 + 1
            dp[s + 1][n + 1] = dp[s][n] + 1
        else:
            # 같은 문자가 아니면 word1, word2에서 문자 하나 뺀 것
            # word2, word1에서 문자 하나 뺀 것과 비교 후 큰 값 삽입
            dp[s + 1][n + 1] = max(dp[s][n + 1], dp[s + 1][n])
print(dp[N1][N2])