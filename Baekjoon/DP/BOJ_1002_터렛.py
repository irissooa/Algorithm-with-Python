'''
조규현의 좌표(x1,y1)과 백승환의 좌표(x2,y2) 류재명과의 각각 거리 r1,r2
류재명이 있을 수 있는 좌표 수 출력
4가지 경우가 있다(일치, 한점으로 접하는경우, 접하지 않는 경우, 두점으로 접하는 경우)
경우를 나눠서 구함
1. distance = 두원의 거리를 이용(x의 차**2 + y의 차**2 의 제곱근
2.  1) distance가 0이고, 반지름이 일치할 경우 일치,
2) abs(r1-r2) 가 distance(내접) or distance = r1+r2(외접)
3) abs(r1-r2) < distance < r1+r2 두점에서 만날때
4) 그외
'''
import math, sys
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    possible = 0
    # 일치
    if dist == 0 and r1 == r2:
        possible = -1
    # 외접 또는 내접
    elif dist == r1+r2 or dist == abs(r1-r2):
        possible = 1
    # 두 점에서 만남
    elif abs(r1-r2) < dist < r1+r2:
        possible = 2
    # 만나지 않음
    else:
        possible = 0
    print(possible)
