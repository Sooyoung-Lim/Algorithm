import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    matrix_T = list(zip(*matrix))
    print(matrix_T)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if len(set(matrix[i])) == 9 and len(set(matrix_T[i])) == 9:

    while i
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(0, 3):
                if matrix[i:i+k][j:j+k]:

