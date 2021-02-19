# 충전소가 있는 정류소만 보는 방식
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점인 정류장(정류장 총 갯수)
    # M : 충전기가 설치된 정류장의 갯수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    # 시점과 종점을 추가하자.
    charge = [0] + charge + [N]
    # charge.insert(0,0)
    # charge.append(N)

    last = 0
    ans = 0

    # 충전소에 출발점과 도착지를 넣어놓았으므로
    for i in range(1, M+2):
        if charge[i] - charge[i-1] > K:
            ans = 0
            break

        # 갈 수 있으면 아무작업 X
        # 갈 수 없다면 내 바로직전 충전소로 위치를 옮기고 횟수 1회 증가
        if charge[i] > last+K:
            last = charge[i-1]
            ans += 1


    print('#{} {}'.format(tc, ans))