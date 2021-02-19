import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점인 정류장(정류장 총 갯수)
    # M : 충전기가 설치된 정류장의 갯수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    bus_stop = [0] * (N+1)

    # 충전소를 표시하자-방법1
    # for i in range(M):
    #     bus_stop[charge[i]] = 1

    # 충전소를 표시하자-방법2
    for i in charge:
        bus_stop[i] = 1

    bus = 0 # 버스 위치
    ans = 0 # 충전 회수

    while True:
        # 버스가 이동할 수 있는 만큼 이동하자
        bus += K
        if bus >= N : break # 종점에 도착하거나, 종점을 지나 더 나아간 경우

        for i in range(bus, bus-K, -1):
            if bus_stop[i] == 1:
                ans += 1
                bus = i
                break
        # 충전기를 못찾았을 때
        else:
            ans = 0
            break


    print('#{} {}'.format(tc, ans))