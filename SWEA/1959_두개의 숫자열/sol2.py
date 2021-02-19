# 내 방법이 다소 번거로우므로, 겹치는 부분을 함수로 한번만 구현해서 써먹어보자
import sys
sys.stdin = open('input.txt')

def check(long, short):
    max_value = -98765332
    for i in range(len(long) - len(short)+1) :
        result = 0
        for j in range(len(short)):
            result += long[i+j] * short[j]

        if max_value < result:
            max_value = result

    return result

T = int(input())

for tc in range(1, T+1):
    # N: 문자열 A의 갯수
    # M: 문자열 B의 갯수
    N, M = map(int, input().split())
    numbers_A = list(map(int, input().split()))
    numbers_B = list(map(int, input().split()))

    if N > M:
        ans = check(numbers_A, numbers_B)
    else:
        ans = check(numbers_B, numbers_A)

    print("{} {}".format(tc, ans))
