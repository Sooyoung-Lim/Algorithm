import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    T = int(input())
    matrix = [list(map(int, input().split())) for i in range(100)]

    # 가로 합
    max_row = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += matrix[i][j]
        if sum > max_row:
            max_row = sum

    # 세로 합
    max_col = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += matrix[j][i]
        if sum > max_col:
            max_col = sum

    # 대각선 합
    max_diagonal = 0
    for i in range(100):
        sum1 = 0
        sum2 = 0
        # 왼쪽 위 -> 오른쪽 아래
        sum1 += matrix[i][i]
        # 오른쪽 위 -> 왼쪽 아래
        sum2 += matrix[i][99-i]
    if max(sum1, sum2) > max_diagonal:
        max_diagonal = max(sum1, sum2)

    result = max(max_row, max_col, max_diagonal)

    print("#{} {}".format(tc, result))

