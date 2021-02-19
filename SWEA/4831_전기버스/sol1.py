import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점인 정류장(정류장 총 갯수)
    # M : 충전기가 설치된 정류장의 갯수
    K, N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    stations = [0] * (N+1)
    for number in numbers:
        stations[number] += 1

    # 방법 1) K 개씩 가다가 1이 아니면 하나 빽, 빽, 빽해서 확인
    # 방법 2) 하나씩 순차적으로 가면서 확인하는 방법. k안에서 나오는 정류소를 저장하고 장
    # 만약 더 있으면 그 더있는걸로 바꿔서 저
    start = 0
    end = K
    count = 0

    while True:
        zero = 0
        for i in range(start+1, end+1):
            if stations[i] == 1:
                start = i
            else:
                zero += 1
        if zero == K:
            count = 0
            break
        count += 1
        end = start + K

        if end >= N:
            break

    print('#{} {}'.format(tc, count))
