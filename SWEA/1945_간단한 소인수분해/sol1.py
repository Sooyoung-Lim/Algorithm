import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    prime_factor = [0] * 5
    while N > 1:
        if N % 2 == 0:
            N = N/2
            prime_factor[0] += 1

        if N % 3 == 0:
            N = N/3
            prime_factor[1] += 1

        if N % 5 == 0:
            N = N/5
            prime_factor[2] += 1

        if N % 7 == 0:
            N = N/7
            prime_factor[3] += 1

        if N % 11 == 0:
            N = N/11
            prime_factor[4] += 1

        result = prime_factor

    print('#{} '.format(tc), end='')
    print(*prime_factor)
