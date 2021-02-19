import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    count = [0] * 5

    for i in range(len(prime)):
        while N % prime[i] == 0:
            count[i] += 1
            N //= prime[i]

    print('#{} {}'.format(tc, " ".join(map(str, count))))
