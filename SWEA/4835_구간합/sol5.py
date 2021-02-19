# 중복된 연산 피하는 방법
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 정수의 갯수
    # M: 구간의 길이
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    tmp = 0
    # 첫 구간은 구해두자
    for i in range(M):
        tmp += numbers[i]

    max_value = tmp
    min_value = tmp

    # 새로운 구간의 합
    for i in range(M, N):
        tmp = tmp + numbers[i] - numbers[i - M]

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print('#{} {}'.format(tc, max_value - min_value))