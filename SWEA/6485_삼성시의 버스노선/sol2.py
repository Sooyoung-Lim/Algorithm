import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 버스 대수

    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        # 해당 정류장에 지나는 버스의 대수 누적
        for j in range(A, B+1):
            bus_stop[j] += 1

    P = int(input())
    # 줄 안바꾸고 출력하고 싶으니
    print('#{}'.format(tc, end=" "))

    for i in range(P):
        C = int(input()) # 우리가 확인하고 싶은 정류장의 번호
        print(bus_stop[C], end=" ")
    # 다음 테스트 케이스부터는 줄 바꿔
    print()