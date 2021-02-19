import sys
sys.stdin = open('input.txt')

def solution(matrix):
    N = len(matrix)
    nxt = 'u'
    r = N-1
    for c in range(N):
        last_row = matrix[r]
        if last_row[c] == 2:
            while r > 0:
                # 올라갈 때는 좌/우회전 우선
                if nxt == 'u':
                    if c < N-1 and matrix[r][c+1] != 0:
                        nxt = 'r'
                        c += 1
                    elif c > 0 and matrix[r][c-1] != 0:
                        nxt = 'l'
                        c -= 1
                    else:
                        r -= 1

                # 옆으로 가는 중일때는 위로 올라갈 수 있는지를 봐야함
                else:
                    if matrix[r-1][c] :
                        nxt = 'u'
                    elif nxt == 'r':
                        c += 1
                    elif nxt == 'l':
                        c -= 1
            return c


T = 10
N= 100
for _ in range(1, T+1):
    tc = int(input())
    print('#{} {}'.format(tc, c))
