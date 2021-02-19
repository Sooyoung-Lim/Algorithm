import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    matrix = [list(input().split()) for _ in range(5)]
    print(matrix)

    result = ''
    for j in range(len(matrix[0][0])):
        word = ''
        for i in range(5):
            if matrix[i][0][j] == False:
                continue
            else:
                word += matrix[i][0][j]
        result += word
    print(result)
