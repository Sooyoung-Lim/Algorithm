import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    dump = int(input())
    numbers = list(map(int, input().split()))
    while dump:
        # 가장 큰 값을 가지는 인덱스를 찾고, 그 인덱스에 해당하는 수를 1 줄이기
        numbers[numbers.index(max(numbers))] -= 1
        # 가장 작은 값을 가지는 인덱스를 찾고, 그 인덱스에 해당하는 수를 1 늘리기
        numbers[numbers.index(min(numbers))] += 1
        dump -= 1

    print('#{} {}'.format(tc, max(numbers) - min(numbers)))