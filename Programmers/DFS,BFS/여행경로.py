'''
1. tickets가 주어지고, [출발,도착]으로 진행됨
2. 갔던곳은 방문표시, 전부 방문한다면 temp에 일단 넣고 알파벳이 더빠른것을 answer로 출력
'''
def solution(tickets):
    answer = []
    def DFS(cnt, idx):
        visited[idx] = True
        if cnt == len(tickets):
            return

    for i in range(len(tickets)):
        visited = [False]*len(tickets)
        DFS(1,i)

    return answer


print(solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]))