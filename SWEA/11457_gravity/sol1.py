import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(numbers)

    matrix = [[0] * N for _ in range(N)]
    # print(matrix)

    for i in range(N):
        for j in range(i):



    for c in numbers:
        for r in range(N-1):
            matrix[r][c] = numbers[N-1-r][c]
    print(matrix)