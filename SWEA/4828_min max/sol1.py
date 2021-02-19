import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 이 문제는 max 와 min 함수를 쓰지않고 그것들을 구현할 줄 아는가를 물어보는 문제
    big = numbers[0]
    for number in numbers:
        if number > big:
            big = number

    small = numbers[0]
    for number in numbers:
        if number < small:
            small = number

    diff = big - small

    print('#{} {}'.format(tc, diff))