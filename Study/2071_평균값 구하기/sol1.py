import sys
sys.stdin = open('input.txt')
#여기까진 제출할 땐 없애야

T = int(input())

for tc in range(1, T+1):
# 여기까지 고정
    numbers = list(map(int, input().split()))
    total = 0
    for idx in range(len(numbers)):
        total += numbers[idx]
    avg = round(total / len(numbers))
    print('#{} {}'.format(tc, avg))
