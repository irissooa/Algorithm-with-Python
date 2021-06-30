'''
array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬, k번째수
commands = [i,j,k]의 배열
'''
def solution(array, commands):
    answer = []
    for command in commands:
        temp = sorted(array[command[0]-1:command[1]])
        answer.append(temp[command[2]-1])
    return answer