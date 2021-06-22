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