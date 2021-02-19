
import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,11):
    test = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]
    dr = N-1
    dc = ladder[N-1].index(2)
    count = 0
    move = 0 # 0=위 1=왼쪽 2=오른. 전 회차의 움직임을 나타내는 변수
    while dr > 0:
        # 전 회차에서, 올라온 상태이거나 왼쪽으로 온 상태인 상황.
        # 왼쪽을 탐색해서 자리있으면 한번 더 간다.
        if (move==0 or move==1) and dc>0 and ladder[dr][dc-1]:
            dc -= 1
            move = 1
        # 전 회차에서, 올라온 상태이거나 오른쪽으로 온 상태인 상황.
        # 오른쪽을 탐색해서 자리 있으면 한번 더 간다.
        elif (move==0 or move==2) and dc<N-1 and ladder[dr][dc+1]:
            dc += 1
            move = 2
        # 위로 up.
        else:
            dr -= 1
            move = 0
    print('#{} {}'.format(tc, dc))