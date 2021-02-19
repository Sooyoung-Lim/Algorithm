import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 정수의 갯수
    # M: 구간의 길이
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_value = 0
    min_value = 2000000
    # M개씩 끊어서 더할꺼니까 range의 마지막 값은 N-M+1
    for i in range(N-M+1):
        tmp = 0

        for j in range(M):
            tmp += numbers[i+j]

        if max_value < tmp:
            max_value = tmp

        if min_value > tmp:
            min_value = tmp

    print('#{} {}'.format(tc, max_value-min_value))