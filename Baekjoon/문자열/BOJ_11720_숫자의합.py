'''
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력
'''
N = int(input())
numbers = list(map(int,input()))
print(sum(numbers))