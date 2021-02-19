# 두개 리스트 길이 먼저 비교하고 큰걸 기준으로 잡겠다
# 작은거를 인덱스 0부터 쭉 밀어서 끝까지 움직이고
# 각각의 인덱스 곱한 값을 저장해서 제일 큰 값 찾겠다

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 문자열 A의 갯수
    # M: 문자열 B의 갯수
    N, M = map(int, input().split())
    numbers_A = list(map(int, input().split()))
    numbers_B = list(map(int, input().split()))


    result = -10000000
    if N < M:
        for i in range(M-N+1):
            max = 0
            for j in range(N):
                max += numbers_B[i+j] * numbers_A[j]
            if max > result:
                result = max

    elif N >= M:
        for i in range(N-M+1):
            max = 0
            for j in range(M):
                max += numbers_A[i+j] * numbers_B[j]
            if max > result:
                result = max

    print("{} {}".format(tc, result))



