import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 버스 대수

    dic = {}
    for i in range(5001):
        dic[i] = 0

    for i in range(N):
        start, end = map(int, input().split())
        for j in range(start, end+1):
            dic[j] += 1

    P = int(input())

    result = []
    for i in range(P):
        result.append(dic[int(input())])

    print('#{} {}'.format(tc, ' '.join(map(str, result))))