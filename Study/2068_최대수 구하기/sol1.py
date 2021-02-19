import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    max_value = 0
    for i in range(len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
    print('#{} {}'.format(tc, max_value))